<template>
  <div class="container mx-auto p-4">
    <div v-if="isLoading" class="text-center">
      <p class="text-lg text-neutralDarkGray">Processing payment confirmation...</p>
      <!-- You could add a spinner here -->
    </div>
    <div v-else-if="confirmationMessage"
         :class="isError ? 'bg-red-100 border-errorRed text-errorRed' : 'bg-green-100 border-successGreen text-successGreen'"
         class="p-4 border-l-4 rounded shadow">
      <h1 class="text-2xl font-headings mb-2">{{ isError ? 'Payment Error' : 'Payment Successful!' }}</h1>
      <p>{{ confirmationMessage }}</p>
      <div v-if="!isError && paymentDetails" class="mt-2">
          <p><strong>Internal Payment ID:</strong> {{ paymentDetails.internal_payment_id }}</p>
          <p><strong>External Transaction ID:</strong> {{ paymentDetails.external_transaction_id }}</p>
      </div>
      <nav class="mt-6 space-x-4">
        <router-link to="/" class="text-primaryBlue hover:underline">Go to Homepage</router-link>
        <router-link v-if="!isError && authState.isLoggedIn" to="/account/payment-history" class="text-primaryBlue hover:underline">View Payment History</router-link>
        <router-link v-if="isError" to="/pay" class="text-primaryBlue hover:underline">Try Payment Again</router-link>
      </nav>
    </div>
     <div v-else class="p-4 bg-yellow-100 border-yellow-500 text-yellow-700 rounded shadow">
        <h1 class="text-2xl font-headings mb-2">Missing Information</h1>
        <p>Payment details not found in the URL, or processing failed unexpectedly.</p>
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
import { authState } from '@/store/auth';

const route = useRoute();
const isLoading = ref(true);
const confirmationMessage = ref('');
const paymentDetails = ref(null);
const isError = ref(false);

onMounted(async () => {
  const { internal_payment_id, token } = route.query;

  if (!internal_payment_id) {
    confirmationMessage.value = 'Payment confirmation details are missing (no internal payment ID).';
    isError.value = true;
    isLoading.value = false;
    return;
  }
  if (!token) {
    // This 'token' is from our mock redirect_url in SelectParkingView.vue,
    // simulating a token from PayPal that we'd use to verify.
    confirmationMessage.value = 'Payment confirmation details are missing (no transaction token).';
    isError.value = true;
    isLoading.value = false;
    return;
  }

  try {
    // Simulate calling our backend's /success_callback endpoint
    // This endpoint in the backend would then verify with PayPal and update the payment status
    const response = await fetch(`/api/payment/success_callback?internal_payment_id=${internal_payment_id}&token=${token}`, {
      method: 'GET', // Or POST, depending on your backend route
      headers: { 'Content-Type': 'application/json' },
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || data.details || `HTTP error! status: ${response.status}`);
    }

    confirmationMessage.value = data.message || 'Payment confirmed successfully.';
    paymentDetails.value = data; // Store all returned data
    isError.value = false;

  } catch (err) {
    confirmationMessage.value = `Error processing payment: ${err.message}`;
    isError.value = true;
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
/* Scoped styles */
</style>
