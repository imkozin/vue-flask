import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '@/views/LoginView'
import RegView from '@/views/RegView'
import UserView from '@/views/UserView'
import PageNotFound from '@/views/PageNotFound'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'register',
    component: RegView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserView,
    meta: { requiresAuth: true}
  },
  {
    path: '/:pathMatch(.*)*',
    component: PageNotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const authData = JSON.parse(sessionStorage.getItem('authData'))
    if (authData) {
      next()
    } else {
      next('/login')
    }
  } else {
    next()
  }
})
export default router
