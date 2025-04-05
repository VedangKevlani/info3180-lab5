<template>
    <div class="add-movie-form-view">
      <h1>Create New Movie</h1>
      <MovieForm />
    </div>
  </template>
  
  <script setup>
  // Import the MovieForm component
  import MovieForm from '@/components/MovieForm.vue';
  </script>
  
  <style scoped>
  .add-movie-form-view {
    padding: 20px;
    background-color: #f4f4f4;
  }
  
  h1 {
    color: #333;
  }
  </style>
  