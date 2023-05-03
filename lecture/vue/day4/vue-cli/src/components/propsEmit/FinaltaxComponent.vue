<template>
  <div>
    
    <h2>결정세액: {{ finalTax }}만원</h2>
    <button @click="disCount()">클릭 시 10만원 공제</button>
  </div>
</template>

<script>
export default {
    name: 'FinaltaxComponent',
    props: {
        afterTax: Number,
        taxCredit: Number,
    },
    computed: {
        finalTax() {
            return this.afterTax - this.taxCredit
        }
    },
    methods: {
        disCount() {
            // computed 속성의 데이터는 직접 변경이 기본적으로는 불가능
            // this.finalTax -= 10
            if (this.finalTaxData === 0) {
                this.finalTaxData = this.afterTax - this.taxCredit
            }
        this.finalTaxData -= 10

        // 부모에게 알림
        // 부모가 등록한 이벤트인 get-discount 이벤트를 호출
        this.$emit('get-discount', this.finalTaxData)
        }
    },
    beforeCreate() {

    },
    created() {

    },
}
</script>

<style>

</style>