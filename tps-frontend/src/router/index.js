import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AboutView from '../views/AboutView.vue';
import ServicesView from '../views/ServicesView.vue';
import ParkingView from '../views/ParkingView.vue';
import ContactView from '../views/ContactView.vue';
import LoginView from '../views/LoginView.vue';
import ProfileView from '../views/account/ProfileView.vue';
import PaymentHistoryView from '../views/account/PaymentHistoryView.vue';
import SettingsView from '../views/account/SettingsView.vue';
import { authState } from '@/store/auth'; // Import authState

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'About',
    component: AboutView,
  },
  {
    path: '/services',
    name: 'Services',
    component: ServicesView,
  },
  {
    path: '/parking',
    name: 'Parking',
    component: ParkingView,
  },
  {
    path: '/contact',
    name: 'Contact',
    component: ContactView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/account/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true }
  },
  {
    path: '/account/payment-history',
    name: 'PaymentHistory',
    component: PaymentHistoryView,
    meta: { requiresAuth: true }
  },
  {
    path: '/account/settings',
    name: 'Settings',
    component: SettingsView,
    meta: { requiresAuth: true }
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  }
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !authState.isLoggedIn) {
    // Store the path the user was trying to access
    // if (to.fullPath !== '/') { // Avoid storing login path itself or root
    //   localStorage.setItem('redirectAfterLogin', to.fullPath);
    // }
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;
