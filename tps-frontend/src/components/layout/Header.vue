<template>
  <header class="bg-primaryBlue text-white p-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <div class="text-xl font-headings font-bold">
        TPS Logo
      </div>
      <Navigation />
    </div>
  </header>
</template>

<script>
import Navigation from './Navigation.vue';

export default {
  name: 'AppHeader',
  components: {
    Navigation,
  },
};
</script>

<style scoped>
/* Scoped styles if needed */
</style>
