import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/dgr_period',
    name: 'dgr_period',
    component: () => import('../views/DgrView')
  },

  {
    path: '/dgr_create',
    name: 'dgr_create',
    component: () => import('../views/DgrCreate')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
