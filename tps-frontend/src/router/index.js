import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AboutView from '../views/AboutView.vue';
import ServicesView from '../views/ServicesView.vue';
import ParkingView from '../views/ParkingView.vue';
import ContactView from '../views/ContactView.vue';
import LoginView from '../views/LoginView.vue';

// Account Views
import ProfileView from '../views/account/ProfileView.vue';
import PaymentHistoryView from '../views/account/PaymentHistoryView.vue';
import SettingsView from '../views/account/SettingsView.vue';

// Payment Views
import SelectParkingView from '../views/payment/SelectParkingView.vue';
import PaymentConfirmationView from '../views/payment/PaymentConfirmationView.vue';
import PaymentCancelledView from '../views/payment/PaymentCancelledView.vue';

// Admin Views
import GenerateQrInfoView from '../views/admin/GenerateQrInfoView.vue';
import AdminDashboardView from '../views/admin/AdminDashboardView.vue';
import AdminUserListView from '../views/admin/AdminUserListView.vue';

import { authState } from '@/store/auth';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/about', name: 'About', component: AboutView },
  { path: '/services', name: 'Services', component: ServicesView },
  { path: '/parking', name: 'Parking', component: ParkingView },
  { path: '/contact', name: 'Contact', component: ContactView },
  { path: '/login', name: 'Login', component: LoginView },
  // Account Routes
  { path: '/account/profile', name: 'Profile', component: ProfileView, meta: { requiresAuth: true }},
  { path: '/account/payment-history', name: 'PaymentHistory', component: PaymentHistoryView, meta: { requiresAuth: true }},
  { path: '/account/settings', name: 'Settings', component: SettingsView, meta: { requiresAuth: true }},
  // Payment Routes
  { path: '/pay', name: 'SelectParking', component: SelectParkingView },
  { path: '/payment/confirmation', name: 'PaymentConfirmation', component: PaymentConfirmationView },
  { path: '/payment/cancelled', name: 'PaymentCancelled', component: PaymentCancelledView },
  // Admin Routes
  { path: '/admin/dashboard', name: 'AdminDashboard', component: AdminDashboardView, meta: { requiresAuth: true, requiresAdmin: true }},
  { path: '/admin/users', name: 'AdminUserList', component: AdminUserListView, meta: { requiresAuth: true, requiresAdmin: true }},
  { path: '/admin/generate-qr-info', name: 'GenerateQrInfo', component: GenerateQrInfoView, meta: { requiresAuth: true, requiresAdmin: true }}
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'),
  routes,
  scrollBehavior() {
    return { top: 0 };
  }
});

router.beforeEach((to, from, next) => {
  const needsAuth = to.meta.requiresAuth;
  const needsAdmin = to.meta.requiresAdmin;

  if (needsAuth && !authState.isLoggedIn) {
    // Store intended destination for redirect after login, if not already going to login
    const query = (to.fullPath && to.fullPath !== '/' && to.name !== 'Login') ? { redirect: to.fullPath } : {};
    next({ name: 'Login', query });
  } else if (needsAdmin && !authState.isAdmin) {
    // If user is logged in but not an admin trying to access admin route
    next({ name: 'Home' }); // Or redirect to a specific 'Unauthorized' page or Profile
  } else {
    next();
  }
});

export default router;
