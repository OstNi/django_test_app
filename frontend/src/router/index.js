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
      component: () => import(/* webpackChunkName: "about" */ '../views/DgrView')
    },

    {
      path: '/tw_block',
      name: 'tw_block',
      component: () => import(/* webpackChunkName: "about" */ '../views/TwblockView')
    },

    {
      path: '/twfy',
      name: 'twfy',
      component: () => import(/* webpackChunkName: "about" */ '../views/TwfyView')
    },

    {
      path: '/create_twfy',
      name: 'create_twfy',
      component: () => import(/* webpackChunkName: "about" */ '../views/CreatetwfyView')
    }



  ]

  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })

  export default router