import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    publishedDate: z.date(),
    coverImage: z.string().optional(),
    excerpt: z.string().optional(),
  }),
});

const settings = defineCollection({
  type: 'data',
  schema: z.object({
    phoneNumber: z.string(),
    email: z.string(),
    businessHours: z.string().optional(),
    announcementBar: z.string().optional(),
    officeAddress: z.string().optional(),
  }),
});

export const collections = {
  posts,
  settings,
};
