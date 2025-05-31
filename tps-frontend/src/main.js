import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Imports from src/router/index.js
import './assets/css/tailwind.css'; // Imports Tailwind CSS

const app = createApp(App);

app.use(router); // Use the router

app.mount('#app'); // Mount the app to the #app element in public/index.html
