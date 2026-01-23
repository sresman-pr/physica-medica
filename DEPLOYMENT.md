# Deployment Guide

## Pre-Deployment Checklist

### 1. Environment Variables

Create a `.env.local` file (copy from `.env.local.example`):

```bash
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
NEXT_PUBLIC_SITE_URL=https://physicamedica.com
```

### 2. Content Review

- [ ] Add professional photos to `/public/images/`
- [ ] Create 5-Minute Mobility Guide PDF in `/public/pdfs/`
- [ ] Verify all contact information in `lib/metadata.ts`
- [ ] Update Wim Hof workshop date in `app/wim-hof-method/page.tsx`
- [ ] Replace placeholder testimonials with real ones
- [ ] Update About page with actual Dr. Maks bio/photo

### 3. Google Analytics Setup

1. Create a GA4 property at [analytics.google.com](https://analytics.google.com)
2. Get your Measurement ID (starts with G-)
3. Add to environment variables

### 4. Domain Configuration

Update `lib/metadata.ts` with your production domain:
```typescript
export const siteConfig = {
  url: 'https://physicamedica.com', // Update this
  // ...
};
```

## Deployment to Vercel (Recommended)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo>
git push -u origin main
```

### Step 2: Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: ./
   - **Build Command**: `npm run build`
   - **Output Directory**: .next
   - **Install Command**: `npm install`

### Step 3: Add Environment Variables

In Vercel project settings:
- `NEXT_PUBLIC_GA_MEASUREMENT_ID` → Your GA4 ID
- `NEXT_PUBLIC_SITE_URL` → https://physicamedica.com

### Step 4: Deploy

Click "Deploy" - Vercel will build and deploy automatically.

### Step 5: Custom Domain

1. In Vercel, go to Settings → Domains
2. Add your domain: `physicamedica.com` and `www.physicamedica.com`
3. Update DNS records as instructed by Vercel

## Post-Deployment Tasks

### 1. Test Everything

- [ ] All pages load correctly
- [ ] Contact form works (update with form handler)
- [ ] Mobile CTA buttons work
- [ ] Google Maps loads
- [ ] Lead magnet modal appears
- [ ] Analytics tracking (check GA4 Real-time)

### 2. SEO Setup

1. **Google Search Console**
   - Add property for physicamedica.com
   - Submit sitemap: `https://physicamedica.com/sitemap.xml`
   - Verify ownership via Vercel

2. **Google Business Profile**
   - Link website
   - Ensure NAP (Name, Address, Phone) matches exactly

3. **Local SEO**
   - Submit to Yelp, Healthgrades, etc.
   - Ensure consistent citations

### 3. Performance Testing

- Run [PageSpeed Insights](https://pagespeed.web.dev/)
- Target: 90+ score on mobile and desktop
- Fix any issues found

### 4. Accessibility Check

- Run [WAVE](https://wave.webaim.org/) accessibility checker
- Ensure WCAG 2.1 AA compliance

## Ongoing Maintenance

### Update Workshop Dates

Edit `app/wim-hof-method/page.tsx`:

```typescript
// Line ~10
const nextWorkshopDate = new Date('2026-03-15'); // Update this
```

### Add Blog/News (Future)

Create `app/blog/` directory and add posts as needed.

### Form Integration

The contact form currently logs to console. To connect:

1. Use [Formspree](https://formspree.io/) (easiest)
2. Use [SendGrid](https://sendgrid.com/) with API route
3. Use [Resend](https://resend.com/) for modern email API

Update `app/contact/page.tsx` with your chosen solution.

### Lead Magnet Email Service

Current modal captures email to localStorage. To actually collect emails:

1. **Mailchimp**: Add API integration
2. **ConvertKit**: Use embed forms
3. **SendGrid**: Store in marketing contacts

Update `components/LeadMagnetModal.tsx` with API call.

## Monitoring

### Analytics

Check GA4 regularly for:
- Traffic sources
- Popular pages
- Conversion rates (CTA clicks, form submissions)
- User flow

### Error Monitoring (Optional)

Add [Sentry](https://sentry.io/) for error tracking:

```bash
npm install @sentry/nextjs
```

## Backup

Vercel automatically keeps deployment history. Additionally:

- Keep GitHub as source of truth
- Export GA4 data monthly
- Backup contact form submissions

## Support

For issues:
1. Check Vercel deployment logs
2. Review Next.js documentation
3. Check browser console for errors

---

**Production URL**: https://physicamedica.com (update after deployment)

**Vercel Dashboard**: https://vercel.com/[your-username]/physica-medica
