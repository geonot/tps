<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-headings text-primaryBlue mb-6">Pay for Parking</h1>
    <form @submit.prevent="initiatePayment" class="space-y-4 max-w-lg">
      <div>
        <label for="licensePlate" class="block text-neutralDarkGray mb-1 font-medium">License Plate</label>
        <input type="text" id="licensePlate" v-model="form.license_plate" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required>
      </div>
      <div>
        <label for="lotId" class="block text-neutralDarkGray mb-1 font-medium">Parking Lot ID</label>
        <input type="text" id="lotId" v-model="form.lot_id" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required placeholder="e.g., LOT-A1">
      </div>
      <div>
        <label for="paymentType" class="block text-neutralDarkGray mb-1 font-medium">Payment Type</label>
        <select id="paymentType" v-model="form.payment_type" class="w-full p-2 border border-neutralMediumGray rounded bg-white focus:ring-primaryBlue focus:border-primaryBlue">
          <option value="daily">Daily</option>
          <option value="hourly">Hourly (Placeholder)</option>
          <option value="event">Event (Placeholder)</option>
          <option value="permit_monthly">Monthly Permit (Placeholder)</option>
        </select>
      </div>
      <div>
        <label for="amount" class="block text-neutralDarkGray mb-1 font-medium">Amount (USD)</label>
        <input type="number" id="amount" v-model.number="form.amount" step="0.01" min="0.01" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required placeholder="e.g., 5.00">
      </div>
      <button type="submit" class="bg-primaryBlue text-white py-2 px-4 rounded hover:bg-opacity-80 transition duration-150" :disabled="isLoading">
        {{ isLoading ? 'Processing...' : 'Proceed to Mock PayPal' }}
      </button>
    </form>
    <div v-if="errorMessage" class="mt-4 text-errorRed bg-red-100 p-3 rounded">{{ errorMessage }}</div>
    <div v-if="paymentResponse" class="mt-6 p-4 bg-neutralLightGray rounded shadow">
      <h3 class="font-bold text-lg text-neutralDarkGray mb-2">Mock Payment Initiation Successful:</h3>
      <p><strong class="font-medium">Internal Payment ID:</strong> {{ paymentResponse.internal_payment_id }}</p>
      <p><strong class="font-medium">Mock PayPal ID:</strong> {{ paymentResponse.mock_paypal_payment_id }}</p>
      <p class="mt-2"><strong class="font-medium">Action:</strong> You would normally be redirected to PayPal.</p>
      <p><strong class="font-medium">Simulated Redirect URL (backend):</strong>
        <a :href="paymentResponse.redirect_url" @click.prevent="informUserOfMock" target="_blank" class="text-secondaryTeal hover:underline break-all">
          {{ paymentResponse.redirect_url }}
        </a>
      </p>
      <p class="mt-3 text-sm text-neutralMediumGray">
        (This is a backend URL for the mock. In a real app, it would be a PayPal URL, and these buttons would not be needed after actual redirection.)
      </p>
      <div class="mt-4 space-x-3">
        <button @click="simulateSuccess" class="bg-successGreen text-white py-1 px-3 rounded text-sm hover:bg-opacity-80 transition duration-150">Simulate Successful Payment</button>
        <button @click="simulateCancel" class="bg-accentOrange text-white py-1 px-3 rounded text-sm hover:bg-opacity-80 transition duration-150">Simulate Cancelled Payment</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { authState } from '@/store/auth';

const form = ref({
  license_plate: '',
  lot_id: '',
  payment_type: 'daily',
  amount: null,
  user_id: null
});
const isLoading = ref(false);
const errorMessage = ref('');
const paymentResponse = ref(null);
const router = useRouter();
const route = useRoute(); // Get route instance

onMounted(() => {
  // Check for query parameters to pre-fill the form
  if (route.query.lot_id) {
    form.value.lot_id = route.query.lot_id;
  }
  if (route.query.amount) {
    const parsedAmount = parseFloat(route.query.amount);
    if (!isNaN(parsedAmount)) {
      form.value.amount = parsedAmount;
    }
  }
  if (route.query.payment_type) {
    form.value.payment_type = route.query.payment_type;
  }
});

const informUserOfMock = () => {
  alert("This is a simulated backend URL for the mock payment flow. In a real application, you would be redirected to an actual payment provider like PayPal.");
};

const initiatePayment = async () => {
  // Ensure amount is a number and positive before sending
  if (typeof form.value.amount !== 'number' || isNaN(form.value.amount) || form.value.amount <= 0) {
    errorMessage.value = "Please enter a valid positive amount.";
    return;
  }

  isLoading.value = true;
  errorMessage.value = '';
  paymentResponse.value = null;

  let userIdToSend = null; // Default to null for guest or if not logged in
  if (authState.isLoggedIn && authState.user && authState.user.id) {
    userIdToSend = authState.user.id;
  }

  const payload = {
    ...form.value,
    user_id: userIdToSend, // Send null if guest, otherwise user ID
    amount: String(form.value.amount) // Backend expects string for Decimal conversion
  };
  // Remove user_id from payload if it's null, if backend prefers it that way
  if (payload.user_id === null) {
    delete payload.user_id;
  }


  try {
    const response = await fetch('/api/payment/initiate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || data.details || `HTTP error! status: ${response.status}`);
    }
    paymentResponse.value = data;
  } catch (err) {
    errorMessage.value = err.message;
  } finally {
    isLoading.value = false;
  }
};

const simulateSuccess = () => {
  if (paymentResponse.value) {
    router.push({
      name: 'PaymentConfirmation',
      query: {
        internal_payment_id: paymentResponse.value.internal_payment_id,
        token: paymentResponse.value.mock_paypal_payment_id // 'token' is what PaymentConfirmationView expects
      }
    });
  }
};

const simulateCancel = () => {
   if (paymentResponse.value) {
    router.push({
      name: 'PaymentCancelled',
      query: {
        internal_payment_id: paymentResponse.value.internal_payment_id
      }
    });
  }
};
</script>

<style scoped>
/* Add any specific scoped styles if Tailwind classes are not sufficient */
</style>
