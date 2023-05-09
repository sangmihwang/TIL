import Vue from 'vue'
import VueRouter from 'vue-router'
import TheFirst from '../views/TheFirst.vue'
import TheSecond from '../views/TheSecond.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/first',
    name: 'first',
    component: TheFirst
  },
  {
    path: '/second',
    name: 'second',
    component: TheSecond
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
