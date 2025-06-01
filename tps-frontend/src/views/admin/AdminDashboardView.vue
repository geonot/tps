<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-headings text-primaryBlue mb-6">Admin Dashboard</h1>
    <p class="mb-8 text-neutralMediumGray">Welcome, Admin! Select an option below to manage the application.</p>
    <nav class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <router-link
        to="/admin/users"
        class="block p-6 bg-white rounded-lg shadow hover:shadow-md transition-shadow text-center border border-neutralLightGray hover:border-secondaryTeal">
        <h2 class="text-xl font-semibold text-secondaryTeal mb-2">Manage Users</h2>
        <p class="text-neutralMediumGray text-sm">View and manage user accounts.</p>
      </router-link>

      <router-link
        to="/admin/generate-qr-info"
        class="block p-6 bg-white rounded-lg shadow hover:shadow-md transition-shadow text-center border border-neutralLightGray hover:border-secondaryTeal">
        <h2 class="text-xl font-semibold text-secondaryTeal mb-2">Generate QR Info</h2>
        <p class="text-neutralMediumGray text-sm">Create data for parking lot QR codes.</p>
      </router-link>

      <!-- Add more admin links here as cards -->
      <div class="block p-6 bg-neutralLightGray rounded-lg text-center border border-neutralMediumGray/50">
         <h2 class="text-xl font-semibold text-neutralMediumGray mb-2">More Options (Placeholder)</h2>
        <p class="text-neutralMediumGray text-sm">Future admin functionalities will appear here.</p>
      </div>
    </nav>
  </div>
</template>

<script setup>
// No specific script needed for this simple dashboard navigation page
</script>

<style scoped>
/* Additional styling if needed */
</style>
