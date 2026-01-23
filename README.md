# Physica Medica - Astro Website

Enterprise-level physical therapy website for Physica Medica in Baltimore, MD. Built with Astro for maximum performance and SEO.

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Project Structure

```
physica-medica/
├── src/
│   ├── layouts/
│   │   └── BaseLayout.astro       # Global layout with SEO schemas
│   ├── pages/                     # All site pages (auto-routed)
│   │   ├── index.astro           # Homepage
│   │   ├── about.astro           # About Dr. Maks
│   │   ├── services/             # Service pages
│   │   │   ├── pancafit-class.astro
│   │   │   ├── personal-training.astro
│   │   │   ├── scoliosis.astro
│   │   │   ├── pregnancy-physical-therapy.astro
│   │   │   └── specialty-techniques/
│   │   │       ├── dry-needling-cupping.astro
│   │   │       └── trigger-point-therapy.astro
│   │   ├── wim-hof-method.astro
│   │   ├── reviews.astro
│   │   ├── contact.astro
│   │   └── schedule.astro
│   ├── components/
│   │   ├── Header.astro          # Navigation
│   │   ├── Footer.astro
│   │   ├── MobileCTA.astro       # Sticky mobile CTA bar
│   │   ├── FAQSection.astro      # Reusable FAQ with schema
│   │   └── AuthorByline.astro    # E-E-A-T author signals
│   └── styles/
│       └── global.css            # Custom CSS + Tailwind
├── public/
│   ├── images/                   # Site images (add yours here)
│   ├── _redirects               # 301 redirects (Netlify)
│   └── robots.txt
├── astro.config.mjs             # Astro configuration
├── vercel.json                  # 301 redirects (Vercel)
└── package.json
```

## 🎯 Key Features

### SEO Optimization
- ✅ Advanced JSON-LD schemas on every page (MedicalBusiness, Physician, FAQPage)
- ✅ Comprehensive meta tags (title, description, Open Graph, Twitter Cards)
- ✅ Automatic sitemap generation
- ✅ Mobile-optimized (H1 visible above fold, sticky CTA bar)
- ✅ Voice search optimized FAQ sections
- ✅ 301 redirects from old Wix URLs

### Content Structure
- ✅ Exact clone of original Wix site content
- ✅ Topic siloing for service pages (Hub and Spoke model)
- ✅ E-E-A-T signals (author credentials, expertise)
- ✅ Internal linking ribbons ("You Might Also Like")

### Performance
- ✅ Static site generation (SSG)
- ✅ Minimal JavaScript
- ✅ Critical CSS inlined
- ✅ Image lazy loading
- ✅ Core Web Vitals optimized

## 📝 Before Launch Checklist

### 1. Add Images
Replace placeholder image paths in pages with actual images:

```bash
# Place images in public/images/
public/images/
├── Physica-Medica-logo.jpg
├── dr-maks-headshot.jpg
├── Baltimore-Physical-Therapist-Dry-Needling-Dr-Maks-Birikov.png
├── Baltimore-Physical-Therapist-Wim-Hof-Certified-Dr-Maks-Birikov.png
├── Baltimore-Physical-Therapist-fitness-equipment.png
├── Baltimore-Physical-Therapist-clinic-2023.png
├── Baltimore-Physical-Therapist-Maks-and-Anthony.jpg
├── physica-medica-location.png
├── Baltimore-Physical-Therapist-session.png
├── Baltimore-Physical-Therapist-physica-medica therapy-.png
└── Baltimore-Physical-Therapist-cupping.png
```

Convert images to WebP for better performance:
```bash
npx @squoosh/cli --webp auto public/images/*.{jpg,png}
```

### 2. Verify Redirects
Check actual Wix URLs and update if needed:
- `public/_redirects` (for Netlify)
- `vercel.json` (for Vercel)

### 3. Test Build
```bash
npm run build
npm run preview
```

Visit http://localhost:4321 and test all pages.

### 4. Validate Schemas
Use Google's Rich Results Test:
- https://search.google.com/test/rich-results
- Test homepage, service pages, and About page
- Ensure MedicalBusiness, Physician, and FAQPage schemas validate

## 🌐 Deployment

### Deploy to Vercel (Recommended)
```bash
vercel --prod
```

### Deploy to Netlify
```bash
netlify deploy --prod
```

### Configure Domain
Point `physicamedica.net` to your deployment:
- Vercel: Add custom domain in project settings
- Netlify: Configure custom domain in site settings

## 📊 Post-Launch

### 1. Google Search Console
- Submit sitemap: `https://physicamedica.net/sitemap-index.xml`
- Monitor crawl errors and indexing
- Check rich results appearance

### 2. Performance Monitoring
- Run Lighthouse audits
- Monitor Core Web Vitals
- Target: 95+ scores on mobile and desktop

### 3. Update Review Count
If Google review count changes, update in:
- `src/layouts/BaseLayout.astro` (aggregateRating schema)

## 🛠️ Development

### Tech Stack
- **Framework**: Astro 5
- **Styling**: Tailwind CSS v4
- **Sitemap**: @astrojs/sitemap
- **Image Optimization**: Sharp

### Key Commands
- `npm run dev` - Start dev server at http://localhost:4321
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run astro` - Run Astro CLI commands

### CSS Variables
Custom variables in `src/styles/global.css`:
```css
--color-primary: #1a4d8f;     /* Professional blue */
--color-accent: #d4af37;      /* Gold */
--color-text-primary: #2d2d2d;
--spacing-section: 8rem;      /* Section padding */
```

## 📞 Contact Information

**Physica Medica**
- Address: 800 S Bond St, Baltimore, MD 21231
- Phone: 443-228-8029
- Email: PhysicaMedica@gmail.com

## 📄 License

© 2026 Physica Medica. All rights reserved.
