import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoList from '../components/TodoPage/AllTodoList.vue'
import ImportantTodoList from '../components/TodoPage/ImportantTodoList.vue'
import TodayTodoList from '../components/TodoPage/TodayTodoList.vue'

// import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'all-todo',
    component: AllTodoList
  },
  {
    path: '/important',
    name: 'important-todo',
    component: ImportantTodoList
  },
  {
    path: '/today',
    name: 'today-todo',
    component: TodayTodoList
  },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
