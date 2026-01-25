import { config, fields, collection, singleton } from '@keystatic/core';

export default config({
  storage: {
    kind: 'local',
    // For production with GitHub:
    // kind: 'github',
    // repo: 'your-username/physica-medica'
  },

  collections: {
    posts: collection({
      label: 'Blog Posts',
      slugField: 'title',
      path: 'src/content/posts/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({
          name: {
            label: 'Title',
            validation: { isRequired: true },
          },
        }),
        publishedDate: fields.date({
          label: 'Published Date',
          validation: { isRequired: true },
          defaultValue: { kind: 'today' },
        }),
        coverImage: fields.image({
          label: 'Cover Image',
          directory: 'public/images/blog',
          publicPath: '/images/blog/',
        }),
        excerpt: fields.text({
          label: 'Excerpt',
          description: 'A short description for SEO and blog listings',
          multiline: true,
        }),
        content: fields.markdoc({
          label: 'Content',
          options: {
            image: {
              directory: 'public/images/blog',
              publicPath: '/images/blog/',
            },
          },
        }),
      },
    }),
  },

  singletons: {
    businessInfo: singleton({
      label: 'Business Info',
      path: 'src/content/settings/business-info',
      schema: {
        phoneNumber: fields.text({
          label: 'Phone Number',
          validation: { isRequired: true },
        }),
        email: fields.text({
          label: 'Email Address',
          validation: { isRequired: true },
        }),
        businessHours: fields.text({
          label: 'Business Hours',
          multiline: true,
          description: 'e.g., "Mon-Fri: 9am - 5pm"',
        }),
        announcementBar: fields.text({
          label: 'Announcement Bar',
          description: 'Optional alert message (e.g., "Now accepting new patients")',
        }),
        officeAddress: fields.text({
          label: 'Office Address',
          multiline: true,
        }),
      },
    }),
  },
});
