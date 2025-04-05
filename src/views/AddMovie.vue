<template>
  <form @submit.prevent="submitMovie">
    <input type="text" v-model="title" placeholder="Movie Title" required />
    <textarea v-model="description" placeholder="Description" required></textarea>
    <input type="file" @change="handleFileUpload" required />
    <button type="submit">Submit</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      description: '',
      poster: null
    };
  },
  methods: {
    handleFileUpload(event) {
      this.poster = event.target.files[0];
    },
    getCookie(name) {
      const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
      return match ? match[2] : null;
    },
    async submitMovie() {
      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('poster', this.poster);

      const csrfToken = this.getCookie('csrf_token');

      try {
        const response = await axios.post('http://127.0.0.1:8080/api/v1/movies', formData, {
          headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'multipart/form-data'
          },
          withCredentials: true
        });
        console.log(response.data);
        alert("Movie uploaded!");
      } catch (err) {
        console.error(err.response.data);
        alert("Error uploading movie.");
      }
    }
  }
};
</script>
