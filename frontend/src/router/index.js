import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/users',
    name: 'users',
    component: () => import('../views/UserView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
