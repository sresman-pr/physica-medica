# Quick Start Guide 🚀

## First Time Setup (5 minutes)

### 1. Install Dependencies
```bash
npm install
```

### 2. Create Environment File
```bash
cp .env.local.example .env.local
```

Edit `.env.local` and add your Google Analytics ID (get it from analytics.google.com):
```
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

### 3. Run Development Server
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to see your site!

## Project Structure Overview

```
physica-medica/
├── app/                    # All pages and routes
│   ├── page.tsx           # Home page
│   ├── about/             # About Dr. Maks
│   ├── contact/           # Contact form & map
│   ├── services/          # 4 service pages
│   ├── wim-hof-method/    # Workshop landing
│   └── insurance-guide/   # OON insurance info
├── components/            # Reusable components
├── lib/                   # Utilities (metadata, analytics)
└── public/               # Static files
```

## Common Tasks

### Add an Image
1. Place image in `public/images/`
2. Use in component:
```tsx
<Image src="/images/hero.jpg" alt="Description" />
```

### Update Contact Info
Edit `lib/metadata.ts`:
```typescript
export const siteConfig = {
  phone: '443-228-8029',
  address: {
    street: '800 S Bond St',
    // ...
  }
};
```

### Change Colors
Edit `app/globals.css`:
```css
:root {
  --gold: #D4AF37;  /* Change this */
}
```

### Add a New Page
1. Create `app/new-page/page.tsx`
2. Add to navigation in `components/Header.tsx`
3. Add to sitemap in `app/sitemap.ts`

## Testing Your Changes

### Check Build
```bash
npm run build
```

### Run Linter
```bash
npm run lint
```

### Preview Production Build
```bash
npm run build && npm start
```

## Deploy to Vercel (First Time)

### Option 1: Via GitHub (Recommended)
1. Push code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

2. Go to [vercel.com](https://vercel.com)
3. Click "New Project" → Import from GitHub
4. Add environment variables
5. Click "Deploy"

### Option 2: Vercel CLI
```bash
npm i -g vercel
vercel
```

## Important Files to Customize

Before launching, update these:

1. **`lib/metadata.ts`** - Business info, contact details
2. **`app/wim-hof-method/page.tsx`** - Workshop date (line ~10)
3. **`public/images/`** - Add your photos
4. **`public/pdfs/`** - Add 5-minute mobility guide
5. **All pages** - Replace placeholder testimonials

## Need Help?

- **Build errors?** Check the terminal for specific error messages
- **Styling issues?** Inspect element in browser DevTools
- **React errors?** Read the error message carefully - they're usually helpful!

## Documentation Links

- [Next.js Docs](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Framer Motion](https://www.framer.com/motion/)
- [TypeScript](https://www.typescriptlang.org/docs/)

---

**You're all set!** 🎉

Run `npm run dev` and start building!
