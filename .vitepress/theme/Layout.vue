<script setup lang="ts">
import { useData, useRoute, withBase } from 'vitepress'
import Home from './components/Home.vue'
import Project from './components/Project.vue'

const { frontmatter, theme } = useData()
const route = useRoute()

const nav = [
  { text: 'Portfolio', link: '/', match: (p: string) => p === '/' || p.startsWith('/work/') },
  { text: 'About', link: '/about', match: (p: string) => p.startsWith('/about') },
  { text: 'Contact', link: '/contact', match: (p: string) => p.startsWith('/contact') },
]
const isActive = (m: (p: string) => boolean) => m(route.path)
const isProject = () => route.path.startsWith('/work/')
const year = new Date().getFullYear()
</script>

<template>
  <div class="site">
    <header class="site-header wrap">
      <a class="wordmark" :href="withBase('/')">Salomé Doucet | Portfolio</a>
      <nav class="site-nav">
        <a
          v-for="item in nav"
          :key="item.link"
          :href="withBase(item.link)"
          :class="{ active: isActive(item.match) }"
          >{{ item.text }}</a
        >
      </nav>
    </header>

    <main class="site-main">
      <Home v-if="frontmatter.home" />
      <Project v-else-if="isProject()" />
      <div v-else class="wrap page">
        <Content />
      </div>
    </main>

    <footer class="site-footer wrap">
      <span>All rights reserved. © {{ year }} by Salomé Doucet</span>
      <div class="socials">
        <a
          v-if="theme.instagram"
          :href="theme.instagram"
          target="_blank"
          rel="noopener"
          aria-label="Instagram"
        >
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6">
            <rect x="3" y="3" width="18" height="18" rx="5" />
            <circle cx="12" cy="12" r="4" />
            <circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none" />
          </svg>
        </a>
        <a
          v-if="theme.linkedin"
          :href="theme.linkedin"
          target="_blank"
          rel="noopener"
          aria-label="LinkedIn"
        >
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6">
            <rect x="3" y="3" width="18" height="18" rx="5" />
            <line x1="7" y1="10" x2="7" y2="17" />
            <circle cx="7" cy="7" r="1" fill="currentColor" stroke="none" />
            <path d="M11 17v-4a2.5 2.5 0 0 1 5 0v4M11 10.5V17" />
          </svg>
        </a>
      </div>
    </footer>
  </div>
</template>
