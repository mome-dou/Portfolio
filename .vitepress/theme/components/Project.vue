<script setup lang="ts">
import { useData } from 'vitepress'

const { frontmatter } = useData()
</script>

<template>
  <article class="project">
    <img class="project-hero" :src="frontmatter.cover" :alt="frontmatter.title" />
    <div class="wrap project-body">
      <h1 class="heading-sage">{{ frontmatter.title }}</h1>
      <p class="project-year">{{ frontmatter.year }}</p>
      <div class="project-desc">
        <Content />
      </div>
      <div v-if="frontmatter.gallery?.length" class="project-gallery">
        <img
          v-for="(src, i) in frontmatter.gallery"
          :key="i"
          :src="src"
          :alt="`${frontmatter.title} — image ${i + 1}`"
          loading="lazy"
        />
      </div>
    </div>
  </article>
</template>
