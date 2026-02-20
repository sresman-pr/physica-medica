// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import react from '@astrojs/react';
import markdoc from '@astrojs/markdoc';
import keystatic from '@keystatic/astro';
import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  site: 'https://physicamedica.net',
  adapter: vercel(),
  build: {
    inlineStylesheets: 'always', // Force inline all CSS to eliminate render-blocking
  },
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp',
      config: {
        limitInputPixels: false,
      }
    },
    remotePatterns: [],
  },
  vite: {
    plugins: [tailwindcss()],
    build: {
      cssCodeSplit: false, // Single CSS bundle for easier inlining
      rollupOptions: {
        output: {
          manualChunks: undefined,
        }
      }
    }
  },
  integrations: [
    react(), 
    markdoc(), 
    keystatic(), 
    sitemap({
      serialize(item) {
        // Custom priorities based on page type
        const url = item.url;
        
        // Homepage - highest priority
        if (url === 'https://physicamedica.net/' || url === 'https://physicamedica.net') {
          item.priority = 1.0;
          item.changefreq = 'weekly';
        }
        // Service pages - high priority
        else if (url.includes('/services/') && !url.includes('/specialty-techniques/')) {
          item.priority = 0.9;
          item.changefreq = 'monthly';
        }
        // Condition pages - high priority (SEO targets)
        else if (url.includes('/conditions/')) {
          item.priority = 0.9;
          item.changefreq = 'monthly';
        }
        // Specialty technique pages - high priority
        else if (url.includes('/specialty-techniques/')) {
          item.priority = 0.9;
          item.changefreq = 'monthly';
        }
        // Location pages - good priority
        else if (url.includes('/locations/')) {
          item.priority = 0.8;
          item.changefreq = 'monthly';
        }
        // Blog posts - medium priority
        else if (url.includes('/blog/')) {
          item.priority = 0.7;
          item.changefreq = 'weekly';
        }
        // Other pages - standard priority
        else {
          item.priority = 0.6;
          item.changefreq = 'monthly';
        }
        
        return item;
      }
    })
  ]
});