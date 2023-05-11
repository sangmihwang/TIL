<template>
  <div >
    <h2>할 일 생성 페이지</h2>
    <div>
      <label for="title-input"></label>
      <input id="title-input" type="text" v-model="form.title">
    </div>
    <div>
      <label for="description-input"></label>
      <input id="description-input" type="text" v-model="form.description">
    </div>
    <button @click="goCreate()">생성하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateView',
  data() {
    return {
      form: {
        title: '',
        description: '',
        completed: false,
      }
    }
  },
  methods: {
    goCreate() {
      if(this.form.title === '') {
        alert('할 일을 입력해주세요.')
        return
      }
      if(this.form.description === '') {
        alert('설명을 입력해주세요.')
        return
      }

      // 서버로 전송 -> 결과
      // 생성하는 로직 -> 여기서밖에 안 쓰임
      const BACKEND_URL = 'http://localhost:8000/todos/'
      axios.post(BACKEND_URL, this.form)
      .then(() => {
        // 최소한의 사용자 경험
        alert('정상적으로 생성됨')
        this.form.title = ''
        this.form.description = ''
        // console.log(response)
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>
