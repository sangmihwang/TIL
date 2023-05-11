<template>
  <div>
    <div v-if="todos">
        <div v-for="todo in todos" :key="todo.id" v-bind:class="{completed: todo.completed}" v-on:click="updateTodo(todo)">
            <!-- todo.completed 값이 true 이면 클래스 completed 부여한다 -->
            <!-- <TodoDetail data="data"/> 정적인 데이터일 때 -->
            <!-- 동적인 데이터 -->
            <TodoDetail :todo="todo"/>
            <button v-on:click="deleteTodo(todo)">Delete</button>
        </div>
    </div>
    <div v-else>
      <p>로딩 중..</p>
    </div>
  </div>
</template>

<script>
import TodoDetail from './TodoDetail.vue'
import axios from 'axios'

export default {
    name: 'TodoList',
    components: {
        TodoDetail,
    },
    methods: {
        deleteTodo(todo) {
            const BACKEND_URL = 'http://localhost:8000/todos/'
            const ID = `${todo.id}/`
            axios.delete(BACKEND_URL+ID)
                .then(() => {
                //   todos.splice(todos.id, 1)
                this.refreshTodos()
                })
            },
        refreshTodos() {
            this.$store.dispatch('getTodos')
        },
        
        updateTodo(todo) {
            todo.completed = !todo.completed
            // console.log(todo)
        }
    },
    created() {
        this.$store.dispatch('getTodos')
    },
    computed: {
        todos() {
            return this.$store.state.todos.length === 0 ?
            false : this.$store.state.todos
        }
    }
    
}
</script>

<style>
    .completed{
        text-decoration: line-through;
    }
</style>