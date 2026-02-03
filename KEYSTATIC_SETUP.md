# Keystatic CMS Setup Guide

## Overview

Keystatic CMS has been integrated into your Physica Medica website. This allows you to edit content without touching code through a user-friendly admin interface.

## Accessing the Admin Dashboard

### Local Development

1. Start the development server:
   ```bash
   npm run dev
   ```

2. Navigate to: `http://localhost:4321/keystatic`

3. You'll see the Keystatic admin interface with two main sections:
   - **Blog Posts** - Create and manage blog posts
   - **Business Info** - Update global business information

### Production (After Deployment)

Visit: `https://physicamedica.net/keystatic`

## Features

### 1. Blog Posts Collection

Create and manage blog posts with:
- **Title** - The post title (also generates the URL slug)
- **Published Date** - When the post was published
- **Cover Image** - Featured image for the post
- **Excerpt** - Short description for SEO and blog listings
- **Content** - Rich text editor with formatting options

**Blog URLs:**
- Blog index: `/blog`
- Individual posts: `/blog/[post-slug]`

### 2. Business Info Singleton

Update global business information that appears throughout the site:
- **Phone Number** - Displayed in footer and used in structured data
- **Email Address** - Contact email
- **Business Hours** - Operating hours (supports multiple lines)
- **Announcement Bar** - Optional alert message shown at the top of all pages
- **Office Address** - Physical address (supports multiple lines)

**Where this appears:**
- Footer on all pages
- Announcement bar (if set) at the top of all pages
- Structured data for SEO

## How It Works

### Storage

Content is stored as files in your repository:
- Blog posts: `src/content/posts/[slug]/`
- Business info: `src/content/settings/business-info.yaml`

### Current Mode: Local Storage

The CMS is currently configured for **local storage**, which means:
- Changes are saved directly to files in your repo
- You need to commit and push changes to deploy them
- Only one person can edit at a time

### Switching to GitHub Mode (Recommended for Production)

For multi-user editing and automatic deployments:

1. Update `keystatic.config.ts`:
   ```typescript
   storage: {
     kind: 'github',
     repo: 'your-username/physica-medica'
   }
   ```

2. Set up GitHub OAuth App:
   - Go to GitHub Settings > Developer settings > OAuth Apps
   - Create a new OAuth App
   - Set Authorization callback URL to: `https://physicamedica.net/api/keystatic/github/oauth/callback`
   - Add Client ID and Client Secret to your environment variables

3. With GitHub mode:
   - Changes create commits automatically
   - Multiple users can edit simultaneously
   - Changes deploy automatically via Vercel

## Workflow

### Adding a Blog Post

1. Go to `/keystatic`
2. Click "Blog Posts" in the sidebar
3. Click "Create Blog Post"
4. Fill in the fields:
   - Enter a title (URL slug is auto-generated)
   - Select published date
   - Upload a cover image
   - Write an excerpt
   - Write your content using the rich text editor
5. Click "Save"
6. In local mode: Commit and push the changes
7. The post will appear at `/blog/[slug]`

### Updating Business Info

1. Go to `/keystatic`
2. Click "Business Info" in the sidebar
3. Update any fields you want to change
4. Click "Save"
5. In local mode: Commit and push the changes
6. Changes appear immediately on all pages

### Using the Announcement Bar

The announcement bar is perfect for:
- "Now accepting new patients"
- "Holiday hours: Closed Dec 25-26"
- "Special promotion this month"
- Any time-sensitive message

To enable:
1. Go to Business Info
2. Enter text in "Announcement Bar" field
3. Save

To disable:
1. Clear the "Announcement Bar" field
2. Save

## Image Management

### Blog Images

- Cover images are stored in `public/images/blog/`
- Images in content are also stored in `public/images/blog/`
- Supported formats: JPG, PNG, WebP, GIF
- Recommended size: 1200x630px for cover images

## Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Troubleshooting

### "Collection does not exist" errors during build

This is normal if no content has been created yet. The build will succeed and the pages will work once content is added through the CMS.

### Changes not appearing

**In local mode:**
- Make sure you've saved in Keystatic
- Commit and push your changes
- Vercel will automatically rebuild and deploy

**In GitHub mode:**
- Changes are committed automatically
- Wait for Vercel to rebuild (usually 1-2 minutes)

### Can't access `/keystatic`

- Make sure the dev server is running (`npm run dev`)
- Check that you're using the correct URL
- Clear your browser cache

## Technical Details

### Dependencies Added

- `@keystatic/core` - Core CMS functionality
- `@keystatic/astro` - Astro integration
- `@astrojs/react` - React support (required for admin UI)
- `@astrojs/markdoc` - Rich text editor
- `@astrojs/vercel` - Vercel adapter for SSR admin routes

### Files Created/Modified

**New files:**
- `keystatic.config.ts` - CMS configuration
- `src/content/config.ts` - Content collection schemas
- `src/content/settings/business-info.yaml` - Business info data
- `src/pages/blog/index.astro` - Blog listing page
- `src/pages/blog/[slug].astro` - Individual blog post page
- `src/components/AnnouncementBar.astro` - Announcement bar component

**Modified files:**
- `astro.config.mjs` - Added integrations and adapter
- `src/components/Footer.astro` - Now fetches data from CMS
- `src/layouts/BaseLayout.astro` - Added announcement bar

## Support

For questions about:
- **Using Keystatic**: See [Keystatic documentation](https://keystatic.com/docs)
- **Astro content collections**: See [Astro documentation](https://docs.astro.build/en/guides/content-collections/)
- **This implementation**: Contact your developer

## Next Steps

1. ✅ Test the admin interface at `/keystatic`
2. ✅ Create your first blog post
3. ✅ Update business information
4. ✅ Test the announcement bar
5. ⬜ Consider switching to GitHub mode for production
6. ⬜ Add more blog posts regularly for SEO
