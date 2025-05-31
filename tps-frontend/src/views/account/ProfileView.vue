<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-headings text-primaryBlue">User Profile</h1>
    <p v-if="authState.isLoggedIn && authState.user">Welcome, {{ authState.user.username }}!</p>
    <p v-else>Please log in to view your profile.</p>
    <nav class="mt-4">
      <router-link to="/account/payment-history" class="mr-4 text-secondaryTeal hover:underline">Payment History</router-link>
      <router-link to="/account/settings" class="text-secondaryTeal hover:underline">Account Settings</router-link>
    </nav>
  </div>
</template>
<script setup>
import { authState } from '@/store/auth';
</script>
