import { forEach } from 'core-js/core/array'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?americano>'
      },
      {
        title: '라떼',
        price: 4000,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?latte>'
      },
      {
        title: ' 카푸치노',
        price: 4500,
        selected: false, // 초기값
        image: '<https://source.unsplash.com/featured/?capuccino>'
      }
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false, //초기값
      },
      {
        name: 'medium',
        price: 700,
        selected: false, //초기값
      },
      {
        name: 'large',
        price: 1000,
        selected: false, //초기값
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {
      
    },
    updateMenuList: function (state, selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu.title === selectedMenu.title) {
          menu.selected = true
        } 
      })
      }
    },
    updateSizeList: function (state, selectedSize) {
      state.sizeList.forEach((size) => {
        if (size.name === selectedSize.name) {
          size.selected = true
        } 
      })
    },
  actions: {
  },
  modules: {
  }
})