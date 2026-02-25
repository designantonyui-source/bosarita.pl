# SEO Optimization Strategy - Bosarita Poznań

This document outlines the recommended SEO improvements for the Bosarita photography portfolio website.

## 1. Technical SEO Recommendations

### 1.1. Title & Meta Enhancements
- **Current State:** Many titles are generic (e.g., "Sesja rodzinna").
- **Recommendation:** Use a consistent format: `[Service Name] Poznań - Bosarita Fotograf`.
- **Target Keywords:** "Fotograf rodzinny Poznań", "Sesja noworodkowa Poznań", "Fotografia plenerowa Poznań".

### 1.2. Meta Description Optimization
- **Recommendation:** Each page should have a unique, compelling description (150-160 characters) that includes a call to action.

### 1.3. Open Graph & Social Sharing
- **Current State:** Missing OG tags.
- **Recommendation:** Add `og:title`, `og:description`, `og:image`, and `og:url` to all pages to ensure professional previews when shared on Facebook, Instagram, or WhatsApp.

### 1.4. Robots.txt
- **Current State:** Missing.
- **Recommendation:** Add a `robots.txt` file to guide search engine crawlers.

### 1.5. Schema.org Enhancement
- **Current State:** Basic `LocalBusiness` schema is present on the homepage.
- **Recommendation:** 
    - Add `AggregateRating` if you have Google Reviews.
    - Add `Service` schema for each specific session type.
    - Implement `BreadcrumbList` schema for better SERP visibility.

## 2. Content & Keyword Strategy

### 2.1. Heading Hierarchy
- **Recommendation:** Ensure only one `<h1>` per page. Use `<h2>` for section titles and `<h3>` for subsections.
- **Action:** Update the homepage `<h1>` to include more specific keywords.

### 2.2. NLP & Semantic Content
- **Recommendation:** Add 2-3 paragraphs of descriptive text to each service page. Discuss the experience, locations in Poznań, and what the client can expect. This helps with semantic search (LSI keywords).

## 3. Image Optimization (Crucial for Photography)

### 3.1. Alt Text Improvements
- **Current State:** Filenames like `rodzianna-22` are used as alt text.
- **Recommendation:** Use descriptive alt text that includes keywords: "Naturalna sesja rodzinna w plenerze Poznań - Bosarita".

### 3.2. File Naming
- **Recommendation:** Rename image files to be SEO-friendly (e.g., `fotograf-pozna-sesja-rodzinna.jpg`) before uploading. *Note: This requires updating references in HTML.*

### 3.3. Lazy Loading & Formats
- **Status:** Already using lazy loading.
- **Recommendation:** Consider serving WebP versions of all images (not just some) for even faster load times.

## 4. Local SEO Focus

### 4.1. Google Business Profile
- **Recommendation:** Ensure the information on the website (address, phone) exactly matches your Google Business Profile (NAP consistency).

### 4.2. Local Keywords
- **Recommendation:** Include mentions of specific neighborhoods or iconic locations in Poznań (np. Cytadela, Park Sołacki, Stary Rynek) to rank for hyper-local searches.

---

## Priority Implementation Plan

1. **Phase 1 (Immediate):** Update Title tags and Meta Descriptions. Add OG tags.
2. **Phase 2:** Clean up Image Alt tags and titles in `sitemap.xml`.
3. **Phase 3:** Expand text content on service pages for better keyword indexing.
4. **Phase 4:** Implement advanced Schema.org for services and breadcrumbs.
