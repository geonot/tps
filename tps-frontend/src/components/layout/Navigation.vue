<template>
  <nav class="flex items-center space-x-4">
    <router-link to="/" class="text-white hover:text-secondaryTeal">Home</router-link>
    <router-link to="/about" class="text-white hover:text-secondaryTeal">About</router-link>
    <router-link to="/services" class="text-white hover:text-secondaryTeal">Services</router-link>
    <router-link to="/parking" class="text-white hover:text-secondaryTeal">Parking</router-link>
    <router-link to="/contact" class="text-white hover:text-secondaryTeal">Contact</router-link>

    <div class="flex items-center space-x-4 ml-auto"> <!-- Pusher for right alignment of auth links -->
      <template v-if="authState.isLoggedIn">
        <router-link
          v-if="authState.isAdmin"
          to="/admin/dashboard"
          class="text-white hover:text-accentOrange px-3 py-1 rounded-md bg-secondaryTeal hover:bg-opacity-90 transition-colors">
          Admin
        </router-link>
        <router-link
          to="/account/profile"
          class="text-white hover:text-secondaryTeal">
          Profile
        </router-link>
        <button
          @click="handleLogout"
          class="text-white hover:text-secondaryTeal bg-transparent border-none cursor-pointer px-3 py-1">
          Logout
        </button>
      </template>
      <template v-else>
        <router-link
          to="/login"
          class="text-white hover:text-secondaryTeal bg-accentOrange hover:bg-opacity-80 px-3 py-1 rounded-md">
          Login
        </router-link>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { authState, logoutUser } from '@/store/auth';

const router = useRouter();

const handleLogout = () => {
  logoutUser();
  router.push({ name: 'Login' }); // Redirect to Login page after logout
};
</script>

<style scoped>
.router-link-exact-active {
  font-weight: bold;
  /* Example: text-decoration: underline; */
}

button {
  padding: 0;
  display: inline-flex;
  align-items: center;
}
</style>
