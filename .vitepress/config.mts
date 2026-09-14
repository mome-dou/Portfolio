import { defineConfig, type HeadConfig } from 'vitepress'

// Absolute site URL — used to build the Open Graph / Twitter links that make
// shared links show a title, description and preview image.
// ▸ Set this to the real domain before launch.
const SITE = 'https://salomedoucet.com'

export default defineConfig({
  title: 'Salomé Doucet | Portfolio',
  description: 'Portfolio of industrial designer Salomé Doucet.',
  lang: 'en',
  cleanUrls: true,
  srcExclude: ['AGENTS.md', 'PROJECT.md', 'README.md'],
  themeConfig: {
    // ▸ Salomé: your links live here. Update them and the footer/contact follow.
    email: 'salome.doucet@gmail.com',
    instagram: 'https://www.instagram.com/', // TODO: set the real profile URL
    linkedin: 'https://www.linkedin.com/', // TODO: set the real profile URL
  },
  // Per-page SEO: reads `title`, `description` and `cover` from each page's
  // frontmatter and emits social-share tags. Non-engineer surface = frontmatter.
  transformPageData(pageData) {
    const fm = pageData.frontmatter
    const path = pageData.relativePath.replace(/(?:^|\/)index\.md$/, '/').replace(/\.md$/, '')
    const url = `${SITE}/${path}`.replace(/\/+$/, '/')
    const title = fm.title ? `${fm.title} — Salomé Doucet` : 'Salomé Doucet | Portfolio'
    const description = fm.description ?? 'Portfolio of industrial designer Salomé Doucet.'
    const image = fm.cover ? `${SITE}${fm.cover}` : `${SITE}/img/og-default.jpg`

    const head: HeadConfig[] = (fm.head ??= [])
    head.push(
      ['meta', { name: 'description', content: description }],
      ['meta', { property: 'og:type', content: 'website' }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { property: 'og:image', content: image }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }],
      ['meta', { name: 'twitter:image', content: image }],
    )
  },
})
