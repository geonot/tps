import { reactive } from 'vue';

export const authState = reactive({
  isLoggedIn: false,
  user: null // To store user info later
});

export function loginUser(userData) {
  authState.isLoggedIn = true;
  authState.user = userData;
}

export function logoutUser() {
  authState.isLoggedIn = false;
  authState.user = null;
}
