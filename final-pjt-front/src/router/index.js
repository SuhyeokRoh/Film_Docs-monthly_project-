import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/accounts/Signup'
import LoginView from '@/views/accounts/Login'
import HomeView from '@/views/HomeView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
