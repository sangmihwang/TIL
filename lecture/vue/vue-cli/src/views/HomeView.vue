<template>
<div>
<h1>Home View</h1>
  <TodoList />

</div>
    
</template>

<script>
import TodoList from '../components/TodoList.vue'

export default {
    components: {
        TodoList,
    }
}
</script>

// scoped: 현재 컴포넌트에만 적용
// 자식에게도 적용 안 됨
<style scoped>
h1 {
    color: red;
}

/* >>> : 딥 셀렉터 (부모 컴포넌트에서 자식 컴포넌트의 CSS로 접근) */
/* /deep/ .h1-child 과 ::v-deep(.h1-child) 도 같은 동작 */
div >>> .h1-child {
    color: green;
}
</style>