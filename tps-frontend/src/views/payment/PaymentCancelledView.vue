<template>
  <div class="container mx-auto p-4">
    <div v-if="isLoading" class="text-center">
      <p class="text-lg text-neutralDarkGray">Processing cancellation...</p>
    </div>
    <div v-else-if="cancellationMessage"
         :class="isError ? 'bg-red-100 border-errorRed text-errorRed' : 'bg-yellow-100 border-yellow-500 text-yellow-700'"
         class="p-4 border-l-4 rounded shadow">
      <h1 class="text-2xl font-headings mb-2">{{ isError ? 'Error' : 'Payment Cancelled' }}</h1>
      <p>{{ cancellationMessage }}</p>
      <div v-if="!isError && paymentDetails" class="mt-2">
          <p><strong>Internal Payment ID:</strong> {{ paymentDetails.internal_payment_id }}</p>
      </div>
      <nav class="mt-6 space-x-4">
        <router-link to="/pay" class="text-primaryBlue hover:underline">Try Payment Again</router-link>
        <router-link to="/" class="text-primaryBlue hover:underline">Go to Homepage</router-link>
      </nav>
    </div>
    <div v-else class="p-4 bg-neutralLightGray rounded shadow">
        <h1 class="text-2xl font-headings mb-2">Missing Information</h1>
        <p>Cancellation details not found in the URL, or processing failed unexpectedly.</p>
        <nav class="mt-6 space-x-4">
          <router-link to="/" class="text-primaryBlue hover:underline">Go to Homepage</router-link>
          <router-link to="/pay" class="text-primaryBlue hover:underline">Try Payment Again</router-link>
        </nav>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isLoading = ref(true);
const cancellationMessage = ref('');
const paymentDetails = ref(null);
const isError = ref(false);

onMounted(async () => {
  const { internal_payment_id } = route.query;

  if (!internal_payment_id) {
    cancellationMessage.value = 'Cancellation details are missing (no internal payment ID).';
    isError.value = true;
    isLoading.value = false;
    return;
  }

  try {
    // Simulate calling our backend's /cancel_callback endpoint
    const response = await fetch(`/api/payment/cancel_callback?internal_payment_id=${internal_payment_id}`, {
      method: 'GET', // Or POST, depending on your backend route
      headers: { 'Content-Type': 'application/json' },
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || data.details || `HTTP error! status: ${response.status}`);
    }

    cancellationMessage.value = data.message || 'Payment cancellation processed.';
    paymentDetails.value = data;
    isError.value = false;

  } catch (err) {
    cancellationMessage.value = `Error processing cancellation: ${err.message}`;
    isError.value = true;
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
/* Scoped styles */
</style>
