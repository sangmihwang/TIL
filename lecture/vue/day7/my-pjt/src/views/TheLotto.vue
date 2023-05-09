<template>
  <div>
    <h2>로 번 추</h2>
    <p>{{ lottoNumbers }}</p>

    <h3>추천 받고 싶은 숫자의 수</h3>
    <input type="number" v-model.number="count" @keyup.enter="goLotto()">
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLotto',
    computed: {
      lottoNumbers() {
        // 1~45 숫자 배열 생성
        const numbers = _.range(1, 46)
        // 6개 랜덤으로 선택
        // const lottoNumbers = _.sampleSize(numbers, 6)
        const lottoNumbers = _.sampleSize(numbers, this.$route.params.count)
        // 보기 좋게 정렬
        const sortedLottoNumbers = _.sortBy(lottoNumbers)
        // 반환
        return sortedLottoNumbers
      }
    },
    data() {
      return {
        count: 6
      }
    },
    methods: {
      goLotto() {
        this.$router.push(`/lotto/${this.count}`).catch(() => {
          console.log('같은 숫자 입력함!')
        })
      }
    },
    created() {
      // 받을 땐 route
      // push로 보낼 땐 router
      console.log(this.$router.params)
    }
}
</script>

<style>

</style>