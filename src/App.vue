<script setup>
import { RouterLink, RouterView } from 'vue-router';
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader />
  <main>
    <!-- RouterView will display the MovieForm component when the '/upload' route is accessed -->
    <RouterView />
  </main>
  <AppFooter />
</template>

<style>
body {
  padding-top: 75px;
}
</style>
