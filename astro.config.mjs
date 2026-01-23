// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://physicamedica.net',
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
  integrations: [sitemap()]
});