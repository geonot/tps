<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-headings text-primaryBlue">User Management</h1>
      <router-link
        to="/admin/dashboard"
        class="text-sm text-secondaryTeal hover:underline">
        &larr; Back to Admin Dashboard
      </router-link>
    </div>

    <div v-if="isLoading" class="text-center py-10">
      <p class="text-neutralDarkGray text-lg">Loading users...</p>
      <!-- Basic spinner -->
      <div class="mt-4 inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-primaryBlue"></div>
    </div>

    <div v-if="apiError" class="bg-red-100 border-l-4 border-errorRed text-errorRed p-4 rounded shadow mb-6">
      <p><strong class="font-semibold">Error:</strong> {{ apiError }}</p>
    </div>

    <div v-if="!isLoading && !apiError && users.length === 0" class="bg-yellow-100 border-l-4 border-yellow-500 text-yellow-700 p-4 rounded shadow">
      <p>No users found.</p>
    </div>

    <div v-if="users.length > 0" class="overflow-x-auto bg-white shadow-md rounded-lg">
      <table class="min-w-full border border-neutralMediumGray/50">
        <thead class="bg-neutralLightGray">
          <tr>
            <th class="py-3 px-5 border-b border-neutralMediumGray/30 text-left text-sm font-semibold text-neutralDarkGray uppercase tracking-wider">ID</th>
            <th class="py-3 px-5 border-b border-neutralMediumGray/30 text-left text-sm font-semibold text-neutralDarkGray uppercase tracking-wider">Username</th>
            <th class="py-3 px-5 border-b border-neutralMediumGray/30 text-left text-sm font-semibold text-neutralDarkGray uppercase tracking-wider">Email</th>
            <th class="py-3 px-5 border-b border-neutralMediumGray/30 text-left text-sm font-semibold text-neutralDarkGray uppercase tracking-wider">Created At</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-neutralMediumGray/20">
          <tr v-for="user in users" :key="user.id" class="hover:bg-primaryBlue/5 transition-colors">
            <td class="py-3 px-5 text-neutralDarkGray text-sm">{{ user.id }}</td>
            <td class="py-3 px-5 text-neutralDarkGray text-sm">{{ user.username }}</td>
            <td class="py-3 px-5 text-neutralDarkGray text-sm">{{ user.email }}</td>
            <td class="py-3 px-5 text-neutralDarkGray text-sm">{{ formatDate(user.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const users = ref([]);
const isLoading = ref(false);
const apiError = ref('');

const fetchUsers = async () => {
  isLoading.value = true;
  apiError.value = '';
  try {
    // Assumes proxy is set up for /api prefix, and backend route is /admin/users
    const response = await fetch('/api/admin/users');
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ error: 'Failed to fetch users and parse error details from server.' }));
      throw new Error(errorData.error || errorData.details || `HTTP error ${response.status}`);
    }
    users.value = await response.json();
  } catch (err) {
    apiError.value = err.message;
    users.value = []; // Clear users on error
  } finally {
    isLoading.value = false;
  }
};

const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

onMounted(fetchUsers);
</script>

<style scoped>
/* Scoped styles if needed */
</style>
