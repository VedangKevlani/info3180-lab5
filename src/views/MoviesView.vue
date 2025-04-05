<template>
    <div class="header">
        <h1>Movies</h1>
    </div>
    <div class="container mt-4">
      <div class="row g-4">
        <div class="col-12 col-sm-6 col-lg-4" v-for="movie in movies" :key="movie.id">
          <div class="card h-100 d-flex flex-row">
            <img
              :src="movie.poster"
              class="img-fluid"
              alt="Movie Poster"
              style="width: 180px; height: auto; object-fit: cover;"
            />
            <div class="card-body">
              <h5 class="card-title" style="white-space: normal; word-wrap: break-word;">{{ movie.title }}</h5>
              <p class="card-text" style="white-space: normal;">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
   

<script setup>
import { ref, onMounted } from "vue";

const movies = ref([]); // reactive property to hold movie list
  const fetchMovies = async () => {
    try {
      const res = await fetch('/api/v1/movies');
      const data = await res.json();
      movies.value = data.movies;
    } catch (error) {
      console.error("Error fetching movies:", error);
    }
  };
  
  onMounted(() => {
  fetchMovies(); // call on mount
});
  </script>

<style scoped>

.header {
    margin: 10px;
    padding: 20px;
    text-align: center;
    justify-content: center;
}

.card {
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card-img-top {
  height: 300px;
  object-fit: cover;
}

.movie-container {
  padding: 2rem;
}

.page-title {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.movies-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.movie-card {
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 1rem;
  width: 250px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.movie-poster {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.movie-title {
  font-size: 1.25rem;
  margin-top: 0.5rem;
}

.movie-description {
  font-size: 0.9rem;
  color: #555;
}
</style>