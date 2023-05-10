import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import DogView from '@/views/DogView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)
const isLoggedIn = true

const routes = [
  {
    path: '/404',
    name: '404',
    component: NotFound404
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인함')
        next({ name: 'home'})   // 로그인 되어 있으면 홈으로 이동
      }  {
        next()  // 로그인이 안 되어 있다면 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*', // 그 외의 모든 이상한 url (위에서부터 쭉 내려오다가 암것도 없으면)
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js

// router.beforeEach((to, from, next) => {
//   // CODE HERE
//   // console.log('to', to)
//   // console.log('from', from)
//   // console.log('next', next)
//   // next()  // next()를 써줘야 페이지 이동이 됨

//   // 로그인 여부
//   const isLoggedIn = true
//   // const isLoggedIn = false
//   // false이면(로그인 안 된 상태이면) hello 눌러도 로그인 페이지 이동

//   // 로그인이 필요한 페이지 지정
//   // const authPages = ['hello', 'about', 'home']
//   // 로그인 필요없는 페이지만 제외해도 됨
//   const allowAllPages = ['login']

//   // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAllPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     // 로그인 안 된 상태면 to로 이동
//     console.log('Login으로 이동')
//     next({ name: 'login'})
//   } else {
//     // 로그인해서 가려고 했던 Login 페이지가 to
//     console.log('to로 이동!')
//     next()
//   } 
// })





export default router
