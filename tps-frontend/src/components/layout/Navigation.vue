<template>
  <nav class="flex items-center space-x-4">
    <router-link to="/" class="text-white hover:text-secondaryTeal">Home</router-link>
    <router-link to="/about" class="text-white hover:text-secondaryTeal">About</router-link>
    <router-link to="/services" class="text-white hover:text-secondaryTeal">Services</router-link>
    <router-link to="/parking" class="text-white hover:text-secondaryTeal">Parking</router-link>
    <router-link to="/contact" class="text-white hover:text-secondaryTeal">Contact</router-link>

    <template v-if="authState.isLoggedIn">
      <router-link to="/account/profile" class="text-white hover:text-secondaryTeal">Profile</router-link>
      <button @click="handleLogout" class="text-white hover:text-secondaryTeal bg-transparent border-none cursor-pointer">Logout</button>
    </template>
    <template v-else>
      <router-link to="/login" class="text-white hover:text-secondaryTeal bg-accentOrange hover:bg-opacity-80 px-3 py-1 rounded-md">Login</router-link>
    </template>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { authState, logoutUser } from '@/store/auth';

const router = useRouter();

const handleLogout = () => {
  logoutUser();
  // Redirect to Home page after logout, or to Login page if preferred
  router.push({ name: 'Home' });
};
</script>

<style scoped>
/* Styling for active router links can be added here or globally */
/* Using Tailwind's default active class handling with router-link is often sufficient,
   but custom active styles can be defined if needed. */
.router-link-exact-active {
  /* Example: color: #40B0A6; /* Secondary Teal for active, if different from hover */
  font-weight: bold; /* Or use Tailwind's font-bold class directly in the template */
}

/* Ensure button styling is consistent with links if not using Tailwind button classes */
button {
  padding: 0; /* Reset default button padding if any */
  display: inline-flex; /* Align with links */
  align-items: center;
}
</style>
