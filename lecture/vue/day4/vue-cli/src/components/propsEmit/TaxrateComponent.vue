<template>
  <div>

    <h2>산출세액: {{ afterTax }}만원</h2>
    <h2>세액감면: (-) {{ taxCredit }} 만원</h2>
    <h2>버튼 클릭 후 세금: {{ finalTax }} 만원</h2>

  <FinaltaxComponent
    :after-tax="afterTax"
    :tax-credit="taxCredit"
    @get-discount="getDisCount"
  />

    
  </div>
</template>

<script>
import FinaltaxComponent from './FinaltaxComponent.vue'

export default {
    name: 'TaxrateComponent',
    components: {
        FinaltaxComponent
    },
    data() {
        return {
            finalTax: 0,
        }
    },
    props: {
        taxRate: Number,
        taxCredit: Number,
    },
    computed: {
        afterTax() {
            if(this.taxRate <= 1200) {
                return Math.round(this.taxRate * 0.06)
            }else if(this.taxRate <= 4600) {
                return Math.round(this.taxRate * 0.15) - 108
            }else if(this.taxRate <= 8800) {
                return Math.round(this.taxRate * 0.24) - 522
            }else if(this.taxRate <= 15000) {
                return Math.round(this.taxRate * 0.35) -1490
            }else if(this.taxRate <= 30000) {
                return Math.round(this.taxRate * 0.38) -1940
            }else if(this.taxRate <= 50000) {
                return Math.round(this.taxRate * 0.40) -2540
            }else if(this.taxRate <= 100000) {
                return Math.round(this.taxRate * 0.42) -3540
            }else {
                return Math.round(this.taxRate * 0.45) -6540
            }
        }
    },
    methods : {
        getDisCount(finalTaxData) {
            console.log("자식에게서 호출 옴!")
            console.log(`자식이 보낸 데이터: ${finalTaxData}`)
            this.finalTax = finalTaxData
            // 부모에게 자식의 데이터를 전달
            this.$emit('get-discount', finalTaxData)
        }
    }
}
</script>

<style>

</style>