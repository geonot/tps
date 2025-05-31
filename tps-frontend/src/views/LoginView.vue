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
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { authState, loginUser } from '@/store/auth'; // Using the mock functions

const email = ref('');
const password = ref('');
const router = useRouter();
const errorMessage = ref('');

const handleLogin = async () => {
  // In a real app, this would call an API
  // For now, simulate login
  if (email.value === 'user@example.com' && password.value === 'password') {
    errorMessage.value = ''; // Clear any previous error
    loginUser({ username: 'TestUser', email: email.value }); // Mock user data
    router.push({ name: 'Profile' });
  } else {
    errorMessage.value = 'Invalid credentials (Hint: user@example.com / password)';
  }
};
</script>
