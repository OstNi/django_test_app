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
    path: '/stu_create',
    name: 'stu_create',
    component: () => import('../views/StuStructCreate')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
