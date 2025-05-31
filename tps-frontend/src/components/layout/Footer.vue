<template>
  <footer class="bg-neutralDarkGray text-neutralLightGray p-6 text-center">
    <div class="container mx-auto">
      <p class="mb-2">&copy; {{ new Date().getFullYear() }} Tacoma Parking Services</p>
      <div class="space-x-4">
        <a href="#" class="hover:text-secondaryTeal">Privacy Policy</a>
        <span>|</span>
        <a href="#" class="hover:text-secondaryTeal">Terms of Service</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
};
</script>

<style scoped>
/* Scoped styles if needed */
</style>
