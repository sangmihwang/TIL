<template>
  <div >
    <h2>할 일 목록 페이지</h2>
    <TodoList />
  </div>
</template>

<script>
import axios from 'axios'
import TodoList from '../components/TodoList.vue'

export default {
  name: 'ListView',
  components: {
    TodoList,
  },
  
  created() {
    const BACKEND_URL = 'http://localhost:8000/todos/test/'
    // axios({
    //     method: 'get'
    // }) 이걸 줄여서 아래처럼
    axios.get(BACKEND_URL)
    .then((response) => {
        console.log(response)
    })
    .catch((error) => {
        console.log(error)
    })
  }
}
</script>
