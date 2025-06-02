<template>
  <header class="bg-primaryBlue text-white p-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <div class="flex items-center space-x-3">
        <img 
          :src="logoUrl" 
          alt="TPS Logo" 
          class="h-10 w-auto"
        />
      </div>
      <Navigation />
    </div>
  </header>
</template>

<script>
import Navigation from './Navigation.vue';
import logoImage from '@/assets/logo.jpeg';

export default {
  name: 'AppHeader',
  components: {
    Navigation,
  },
  data() {
    return {
      logoUrl: logoImage
    };
  }
};
</script>

<style scoped>
/* Scoped styles if needed */
</style>
