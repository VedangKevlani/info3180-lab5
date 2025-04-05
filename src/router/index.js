import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AddMovieFormView from '@/views/AddMovieFormView.vue'; // Import AddMovieFormView
import UploadPage from '@/views/UploadPage.vue'; // Import UploadPage

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/movies/create',  // New route for adding a movie
      name: 'AddMovie',
      component: AddMovieFormView, // Use the AddMovieFormView component
    },
    {
      path: '/upload',  // Route for the upload page
      name: 'Upload',
      component: UploadPage,  // Use the UploadPage component
    }
  ]
});

export default router;
