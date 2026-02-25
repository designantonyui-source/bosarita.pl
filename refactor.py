import os
import re

base_path = "/Users/anotny/Downloads/bosarita copy"

for root, dirs, files in os.walk(base_path):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Replace <div class="bloc sticky-nav..."> with <header...>
            content = re.sub(r'<div( class="bloc sticky-nav[^>]*>)', r'<header\1', content)
            # Replace the </div> specifically before <!-- bloc-0 END -->
            content = re.sub(r'</div>\s*<!-- bloc-0 END -->', r'</header>\n\t\t<!-- bloc-0 END -->', content)
            
            # 2. Add <main> around the content blocks
            if '<main>' not in content:
                content = content.replace('<!-- bloc-0 END -->', '<!-- bloc-0 END -->\n\n\t\t<main>')
                content = content.replace('<footer>', '</main>\n\t\t<footer>')
            
            # 3. Change other bloc <divs> into <section>
            content = re.sub(r'<div( class="bloc [^>]*>)', r'<section\1', content)
            # Find all closing divs before <!-- bloc-X END --> (except bloc-0)
            content = re.sub(r'</div>\s*(<!-- bloc-\d+ END -->)', r'</section>\n\t\t\1', content)
            
            # Restore header because it also had class="bloc " and might have matched step 3 if re-run
            content = content.replace('<section class="bloc sticky-nav', '<header class="bloc sticky-nav')
            content = content.replace('</section>\n\t\t<!-- bloc-0 END -->', '</header>\n\t\t<!-- bloc-0 END -->')

            # 4. Change <h3> with h2-style to <h2>
            content = re.sub(r'<h3([^>]*h2-style[^>]*)>(.*?)</h3>', r'<h2\1>\2</h2>', content, flags=re.DOTALL)
            
            # 5. Add aria-labels to image links
            def add_aria(m):
                a_tag = m.group(0)
                if 'aria-label' in a_tag:
                    return a_tag
                alt_match = re.search(r'alt="([^"]+)"', a_tag)
                if alt_match:
                    alt_text = alt_match.group(1).replace('"', '')
                    # Insert aria-label into the <a> tag
                    return a_tag.replace('<a ', f'<a aria-label="Przejdź do: {alt_text}" ', 1)
                return a_tag
                
            # Regex to match <a> tag wrapping an <img>
            content = re.sub(r'<a [^>]*>\s*<img [^>]*>\s*</a>', add_aria, content, flags=re.DOTALL)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Refactored {path}")
