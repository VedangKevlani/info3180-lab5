<template>
  <!-- Form -->
  <form method="POST" enctype="multipart/form-data" @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title:</label>
      <input type="text" id="title" name="title" class="form-control" v-model="formData.title">
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description:</label>
      <textarea id="description" name="description" class="form-control" v-model="formData.description"></textarea>
    </div>

    <!-- Error Message -->
    <div v-if="successMessage" class="message success"> {{ successMessage }} </div>
    <div v-if="errorMessage.length > 0" class="message error">
      <ul>
        <li v-for="(message, index) in errorMessage" :key="index"> {{ message }}</li>
      </ul>
    </div>
    
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster:</label>
      <input type="file" id="poster" name="poster" class="form-control" @change="handleFileChange">
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Define csrf_token as a reactive property
let csrf_token = ref('');

//Define the success_message as a reactive property
const successMessage = ref('');

//Define the success_message as a reactive property
const errorMessage = ref([]);

// Define formData as a reactive reference to an object
const formData = ref({
  title: '',
  description: '',
  poster: null  // Assuming you're handling file uploads
});

// Function to fetch CSRF token
function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
    .catch(error => {
      console.error('Error fetching CSRF token:', error);
    });
}

// Call getCsrfToken when the component is mounted
onMounted(() => {
  getCsrfToken();
});

// Function to handle file change
function handleFileChange(event) {
  formData.poster = event.target.files[0];
}

// Function to handle form submission
function saveMovie() 
{

    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    form_data.append('title', formData.title);
    form_data.append('description', formData.description);
    form_data.append('poster', formData.poster);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        if (!response.ok) {
          
          throw new Error('Network response was not ok'); 

        }
        return response.json();
    })
    .then(function (data) {
        console.log(data);

        // Clear the form data after successful submission
        formData.value = {
            title: '',
            description: ''
        };
        
        // Clear the form data after successful submission, primarly uploads
        movieForm.reset(); // Reset the form
        
        // Clear success message
        successMessage.value = '';

        // Clear error message space before processing the form
        errorMessage.value = []; // Clear error message space before processing the form

        // Show success message
        successMessage.value = 'File Upload Successfully!';

    })
    .catch(function (error) {
        console.error('There was a problem with the fetch operation:', error);
        
        // Clear success message
        successMessage.value = '';

        // Clear error message space before processing the form
        errorMessage.value = []; 

        if (!formData.value.title.trim()) {
            errorMessage.value.push('Error in the Title field - This field is required.');
        }
        if (!formData.value.description.trim()) {
            errorMessage.value.push('Error in the Description field - This field is required.');
        }
        if (!formData.poster) {
            errorMessage.value.push('Error in the Photo field - This field is required.');
        }
          
    });
  
}

</script>

<style scoped>

#movieForm{

  margin: 15px 50px 10px 50px;

}

/* CSS styles for success message */
.success {
  background-color: #7bdb91; /* Green background */
  border-radius: 7px;
  color: white;
  font-size: 12px;
  padding: 12px; /* Adjust padding as needed */
  margin-bottom: 10px; /* Add margin for spacing */
}

/* CSS styles for error message */
.error {
  background-color: #ce7a82; /* Red background */
  border-radius: 7px;
  color: white;
  font-size: 12px;
  padding: 12px; /* Adjust padding as needed */
  margin-bottom: 10px; /* Add margin for spacing */
}

</style>
