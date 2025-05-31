<template>
  <div id="app" class="flex flex-col min-h-screen font-sans">
    <AppHeader />
    <main class="flex-grow">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './components/layout/Header.vue';
import AppFooter from './components/layout/Footer.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style>
/* Global styles can go here if not using a separate CSS file like tailwind.css */
/* Ensure Tailwind's base, components, and utilities are imported, typically in main.js or a main CSS file */
body {
  margin: 0; /* Reset default margin */
  background-color: #FFFFFF; /* Default white background, can be overridden by Tailwind bg classes */
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
