<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-headings text-primaryBlue mb-6">Generate QR Code Link Data</h1>
    <p class="mb-4 text-neutralMediumGray max-w-2xl">
      This page simulates generating the URL that would be embedded in a QR code for a parking lot.
      In a real application, you would use a QR code generation library (e.g., qrcode.vue or similar)
      to display the actual QR code image based on the 'Target URL' below.
    </p>
    <form @submit.prevent="fetchQrLinkData" class="space-y-4 max-w-md bg-white p-6 shadow rounded-lg">
      <div>
        <label for="qrLotId" class="block text-neutralDarkGray mb-1 font-medium">Parking Lot ID</label>
        <input type="text" id="qrLotId" v-model="qrForm.lot_id" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required placeholder="e.g., LOT-B2">
      </div>
      <div>
        <label for="qrAmount" class="block text-neutralDarkGray mb-1 font-medium">Amount (USD)</label>
        <input type="number" id="qrAmount" v-model.number="qrForm.amount" step="0.01" min="0.01" class="w-full p-2 border border-neutralMediumGray rounded focus:ring-primaryBlue focus:border-primaryBlue" required placeholder="e.g., 7.50">
      </div>
      <div>
        <label for="qrPaymentType" class="block text-neutralDarkGray mb-1 font-medium">Payment Type</label>
        <select id="qrPaymentType" v-model="qrForm.payment_type" class="w-full p-2 border border-neutralMediumGray rounded bg-white focus:ring-primaryBlue focus:border-primaryBlue">
          <option value="daily">Daily</option>
          <option value="hourly">Hourly</option>
          <option value="event">Event</option>
        </select>
      </div>
      <button type="submit" class="bg-primaryBlue text-white py-2 px-4 rounded hover:bg-opacity-80 transition duration-150" :disabled="isLoading">
        {{ isLoading ? 'Generating...' : 'Get Link Data' }}
      </button>
    </form>

    <div v-if="apiError" class="mt-4 text-errorRed bg-red-100 p-3 rounded max-w-md">{{ apiError }}</div>

    <div v-if="linkData" class="mt-6 p-6 bg-neutralLightGray rounded shadow max-w-md">
      <h3 class="font-bold text-lg text-neutralDarkGray mb-3">Generated Link Data:</h3>
      <div class="space-y-2">
        <p>
          <strong class="text-neutralMediumGray block">Target URL (for QR Code):</strong>
          <a :href="linkData.target_url" target="_blank" class="text-secondaryTeal hover:underline break-all">{{ linkData.target_url }}</a>
        </p>
        <p>
          <strong class="text-neutralMediumGray block">Content to Encode in QR:</strong>
          <span class="break-all text-sm">{{ linkData.suggested_qr_content }}</span>
        </p>
      </div>
      <div class="mt-4 p-4 bg-white border-2 border-dashed border-neutralMediumGray rounded text-center">
        <p class="text-neutralDarkGray font-semibold text-lg">-- QR Code Placeholder --</p>
        <p class="text-sm text-neutralMediumGray mt-1">
          (Imagine a QR code image here generated from the URL above using a library like 'qrcode.vue')
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const qrForm = ref({
  lot_id: '',
  amount: null,
  payment_type: 'daily'
});
const isLoading = ref(false);
const apiError = ref('');
const linkData = ref(null);

const fetchQrLinkData = async () => {
  isLoading.value = true;
  apiError.value = '';
  linkData.value = null;

  if (typeof qrForm.value.amount !== 'number' || qrForm.value.amount <= 0) {
    apiError.value = "Please enter a valid positive amount.";
    isLoading.value = false;
    return;
  }

  try {
    const response = await fetch('/api/qr/generate_link_data', { // Using proxy
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // Ensure amount is sent as a string if backend expects to parse from string,
      // or as a number if backend handles float directly. Backend currently uses float().
      body: JSON.stringify({ ...qrForm.value, amount: qrForm.value.amount })
    });
    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || data.details || `HTTP error! status: ${response.status}`);
    }
    linkData.value = data;
  } catch (err) {
    apiError.value = err.message;
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
/* Scoped styles if needed */
</style>
