<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-headings text-primaryBlue mb-4">Parking</h1>
    <p class="text-neutralMediumGray mb-6">Find and manage your parking spots, or pay for daily parking.</p>

    <router-link
      to="/pay"
      class="inline-block bg-secondaryTeal text-white py-2 px-6 rounded-lg hover:bg-opacity-80 transition duration-150 text-lg shadow hover:shadow-md">
      Pay for Daily Parking
    </router-link>

    <div class="mt-10">
      <h2 class="text-xl font-headings text-neutralDarkGray">Parking Lots Overview</h2>
      <p class="text-neutralMediumGray mt-2">
        (Placeholder Section) In the future, a list or map of available parking lots will be displayed here.
        Each lot could have options to pay directly or view details.
      </p>
      <!-- Example of how lots might be listed:
      <div class="mt-4 p-4 border rounded-lg shadow-sm">
        <h3 class="text-lg font-semibold text-primaryBlue">Lot A1 - Downtown Central</h3>
        <p class="text-sm text-neutralDarkGray">123 Main St, Tacoma, WA</p>
        <p class="text-sm text-neutralMediumGray">Rates: $2/hr, $10/day</p>
        <router-link
          :to="{ name: 'SelectParking', query: { lot_id: 'LOT-A1', amount: '10.00' } }"
          class="inline-block mt-2 bg-primaryBlue text-white py-1 px-3 rounded text-sm hover:bg-opacity-90">
          Pay for this Lot
        </router-link>
      </div>
      -->
    </div>
  </div>
</template>

<script setup>
// No additional script needed for this basic version
</script>

<style scoped>
/* Add any specific scoped styles if needed */
</style>
