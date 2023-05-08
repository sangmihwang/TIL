import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      // 삭제 버튼 누른 todo 찾아서 state.todos에서 삭제
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1) 
    },
    UPDATE_TODO(state, todoItem) {
      // state.todos = state.todos.map(함수)
      // 함수 => state.todos 배열에서 클릭한 todoitem을 찾고, 해당 todo.isCompleted를 반대로 뒤집는다. true->false 토글!
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {  //내가 클릭한 todoitem을 state.todos 배열에서 찾아서
          todo.isCompleted = !todo.isCompleted // 뒤집
        }
        return todo
      })
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
    },
    updateTodo(context, todoItem) {
      context.commit('UPDATE_TODP', todoItem)
    }
  },
  modules: {
  }
})
