import { reactive } from 'vue';

export const authState = reactive({
  isLoggedIn: false,
  user: null, // e.g., { id: 1, username: 'TestUser', email: 'user@example.com' }
  isAdmin: false // Separate flag for easier checking in guards/nav
});

export function loginUser(userData, isAdmin = false) {
  authState.isLoggedIn = true;
  authState.user = userData;
  authState.isAdmin = isAdmin; // Set admin status
  // console.log('User logged in:', authState); // For debugging
}

export function logoutUser() {
  authState.isLoggedIn = false;
  authState.user = null;
  authState.isAdmin = false; // Reset admin status
  // console.log('User logged out'); // For debugging
}
