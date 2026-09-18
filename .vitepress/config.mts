import { defineConfig, type HeadConfig } from 'vitepress'

// Absolute site URL — used to build the Open Graph / Twitter links that make
// shared links show a title, description and preview image.
// ▸ Set this to the real domain before launch.
const SITE = 'https://salomedoucet.com'
// GitHub Pages subpath (see `base` below). Reset to '/' for the custom domain.
const BASE = '/Portfolio/'

export default defineConfig({
  // TEMPORARY: served as a GitHub Pages project site at
  // mome-dou.github.io/Portfolio/, so assets/links must resolve under that
  // subpath.
  // ▸ TODO before launch: when moving to the salomedoucet.com custom domain
  //   (served at root), set this back to '/' — otherwise every asset 404s.
  base: BASE,
  title: 'Salomé Doucet | Portfolio',
  description: 'Portfolio of industrial designer Salomé Doucet.',
  lang: 'en',
  cleanUrls: true,
  // Coolify's Nixpacks static preset copies /app/dist; VitePress defaults to
  // .vitepress/dist. Emit to ./dist so the deploy COPY finds it. Netlify uses
  // this too — just set publish dir to `dist`.
  outDir: 'dist',
  sitemap: { hostname: SITE },
  srcExclude: ['AGENTS.md', 'PROJECT.md', 'README.md'],
  themeConfig: {
    // ▸ Salomé: your links live here. Update them and the footer/contact follow.
    email: 'salome.doucet@gmail.com',
    instagram: 'https://www.instagram.com/salome_doucet_/',
    linkedin: 'https://www.linkedin.com/in/salom%C3%A9-doucet-06988717a/',
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
    // Preload the above-the-fold hero so it becomes the LCP paint sooner.
    if (fm.cover) head.push(['link', { rel: 'preload', as: 'image', href: `${BASE}${fm.cover}`.replace(/\/{2,}/g, '/') }])
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
