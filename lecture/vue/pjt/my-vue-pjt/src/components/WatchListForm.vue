<template>
  <div>
    <h2>보고싶은 영화</h2>
    <input type="text" v-model="form.title" @keyup.enter="addWishMovie"> 
    <b-button @click="addWishMovie">Add</b-button>
    <div>
      <watch-list-item v-for="(wish, index) in wishList" :key="index" :wish="wish" />
    </div>
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'

export default {
  name: 'WatchListForm',
  components: {
    WatchListItem,
  },
  data() {
    return {
      form: {
        title: '',
      },
      wishList: [],
    }
  },
  methods: {
    addWishMovie() {
      // 프론트에서 최소한의 유효성 검증
      if (this.form.title === '') {
        alert('제목을 입력해주세요!')
        return
      }
      // 보고싶은 영화 생성
      const wish = {
        title: this.form.title,
      }
      this.wishList.push(wish)

      // 폼 초기화
      this.form.title = ''
    }
  }
}
</script>

<style></style>
