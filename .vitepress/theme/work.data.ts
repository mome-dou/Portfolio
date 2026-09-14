import { createContentLoader } from 'vitepress'

export interface ProjectCard {
  url: string
  title: string
  year: number
  cover: string
}

// Build-time index of every work/*.md, newest first — powers the home grid.
// Add a project = add a work/<slug>.md; it shows up here automatically.
declare const data: ProjectCard[]
export { data }

export default createContentLoader('work/*.md', {
  transform: (raw): ProjectCard[] =>
    raw
      .map(({ url, frontmatter }) => ({
        url,
        title: frontmatter.title,
        year: Number(frontmatter.year),
        cover: frontmatter.cover,
      }))
      .sort((a, b) => b.year - a.year || a.title.localeCompare(b.title)),
})
