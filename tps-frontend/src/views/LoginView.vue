<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-headings text-primaryBlue">Login</h1>
    <form @submit.prevent="handleLogin" class="mt-4 space-y-4 max-w-md">
      <div>
        <label class="block text-neutralDarkGray mb-1" for="email">Email</label>
        <input type="email" id="email" v-model="email" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required>
      </div>
      <div>
        <label class="block text-neutralDarkGray mb-1" for="password">Password</label>
        <input type="password" id="password" v-model="password" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required>
      </div>
      <button type="submit" class="bg-primaryBlue text-white py-2 px-4 rounded hover:bg-opacity-80 transition duration-150">Login</button>
    </form>
    <p v-if="errorMessage" class="text-errorRed mt-3">{{ errorMessage }}</p>
    <div class="mt-6 p-3 bg-neutralLightGray rounded max-w-md text-sm">
        <h4 class="font-semibold text-neutralDarkGray mb-1">Test Credentials:</h4>
        <p><strong class="text-neutralMediumGray">Admin:</strong> admin@example.com / password</p>
        <p><strong class="text-neutralMediumGray">User:</strong> user@example.com / password</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router'; // Added useRoute
import { loginUser } from '@/store/auth'; // authState is not directly used here, but loginUser is

const email = ref('');
const password = ref('');
const router = useRouter();
const route = useRoute(); // For accessing query params like 'redirect'
const errorMessage = ref('');

const handleLogin = async () => {
  errorMessage.value = ''; // Clear any previous error
  let redirectTo = route.query.redirect || null; // Get redirect path from query

  if (email.value === 'admin@example.com' && password.value === 'password') {
    loginUser({ id: 99, username: 'AdminUser', email: email.value }, true); // Mock admin user, set isAdmin to true
    // If admin was trying to access a specific admin page, redirect there, else to AdminDashboard
    if (redirectTo && redirectTo.startsWith('/admin')) {
        router.push(redirectTo);
    } else {
        router.push({ name: 'AdminDashboard' });
    }
  } else if (email.value === 'user@example.com' && password.value === 'password') {
    loginUser({ id: 1, username: 'TestUser', email: email.value }, false); // Mock regular user, set isAdmin to false
    // If user was trying to access a specific page, redirect there, else to Profile
    if (redirectTo) {
        router.push(redirectTo);
    } else {
        router.push({ name: 'Profile' });
    }
  } else {
    errorMessage.value = 'Invalid credentials. Please use provided test credentials.';
  }
};
</script>
