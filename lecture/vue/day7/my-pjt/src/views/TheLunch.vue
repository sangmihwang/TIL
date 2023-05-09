<template>
  <div>
    <h2>점 메 추</h2>
    <p>추천 메뉴: {{recommendMenu}} </p>
    <button @click="refresh()">새로고침</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'TheLunch',
    data() {
        return {
            menus: ['제육', '국밥', '만두국', '돈까스']
        }
    },
    computed: {
        recommendMenu() {
            return _.sample(this.menus)
        }
    },
    methods: {
        refresh() {
            // this.$router.push('/lunch')
            // 현재 페이지에서 편재 페이지로 push 요청 시 버그 발생
            // 같은 경로 요청 시도 시 성능이 느려짐
            // 막아놓은 원인 1. 브라우저는 이전 페이지에 대한 정보를 가지고 있음(히스토리)
            //                히스토리에 같은 경로가 또 추가됨
            // 막아놓은 원인 2. 동일한 페이지를 여러 번 방문하는 것이 사용자 경험을 저하함
            //                (사용자의 흐름에 방해됨)
            
            // 새로고침
            // location.reload()

            // 같은 경로 사용 시 막기
            // push, replace 함수들이 Promise 객체 반환
            this.$router.push('/lunch').catch(() => {
                console.log('같은 경로 요청 보냄')
            })
        }
    }
}
</script>

<style>

</style>