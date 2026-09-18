<script setup lang="ts">
import { withBase } from 'vitepress'
import { data as projects } from '../work.data'
</script>

<template>
  <section class="home-grid">
    <a v-for="(p, i) in projects" :key="p.url" class="card" :href="withBase(p.url)">
      <img
        class="card-img"
        :src="withBase(p.cover)"
        :alt="p.title"
        decoding="async"
        :loading="i < 2 ? 'eager' : 'lazy'"
        :fetchpriority="i < 2 ? 'high' : 'auto'"
      />
      <span class="card-title">{{ p.title }}</span>
    </a>
  </section>
</template>
