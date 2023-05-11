<template>
  <div>
    <hr>
    <p>{{ todo.id }} 번째 할 일</p>
    <p>{{ todo.title }}</p>
    
  </div>
</template>

<script>
export default {
    name: 'TodoDetail',
    props: {
        todo: Object,
    }
}
</script>

<style>

</style>