<template>
  <div>
    <h3>모든 할 일</h3>
    <h4 v-for="(item, index) in todoList" :key="index">{{ index+1 }}. {{ item.content }}</h4>
  <hr>
   <h3>Todo</h3>

  <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo()"> 
  <!-- 공백제거: trim -->
  </div>
</template>

<script>
export default {
  name: 'AllTodoList',
  computed: {
      todoList() {
          return this.$store.state.todo.todoList
      }
  },
  data() {
    return {
      todoTitle: ''
    }
  },
  methods: {
    createTodo() {
      console.log(this.todoTitle)
      // 비어 있지 않다면 store에 저장
      if(this.todoTitle){
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      // this.todoTitle 이 비어 있다면 입력하라는 문구 출력
      else {
        alert('todo를 입력하세요')
      }
      this.todoTitle = ''
    }
  },
  created() {
    // 생성 시에 액션 호출
    this.$store.dispatch('loadFromLocalStorage')
  }
}
</script>

<style>

</style>