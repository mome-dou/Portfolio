<script setup lang="ts">
import { useData, withBase } from 'vitepress'
import { computed } from 'vue'

const { frontmatter } = useData()

// A gallery entry is either "/path.jpg" or { src, alt }. Falling back to the
// project title beats "image 1/2/3" for screen readers and SEO — but a real
// per-image description (add `alt:` in the frontmatter) is always better.
type GalleryItem = string | { src: string; alt?: string }
const gallery = computed(() =>
  ((frontmatter.value.gallery ?? []) as GalleryItem[]).map((item) =>
    typeof item === 'string'
      ? { src: item, alt: frontmatter.value.title }
      : { src: item.src, alt: item.alt || frontmatter.value.title },
  ),
)
</script>

<template>
  <article class="project">
    <img
      class="project-hero"
      :src="withBase(frontmatter.cover)"
      :alt="frontmatter.title"
      fetchpriority="high"
      decoding="async"
    />
    <div class="wrap project-body">
      <h1 class="heading-sage">{{ frontmatter.title }}</h1>
      <p class="project-year">{{ frontmatter.year }}</p>
      <div class="project-desc">
        <Content />
      </div>
      <div v-if="gallery.length" class="project-gallery">
        <img
          v-for="(img, i) in gallery"
          :key="i"
          :src="withBase(img.src)"
          :alt="img.alt"
          loading="lazy"
          decoding="async"
        />
      </div>
    </div>
  </article>
</template>
