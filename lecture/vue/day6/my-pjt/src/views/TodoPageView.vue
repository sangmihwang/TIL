<template>
  <div>
    <nav>
      <router-link to="/">모든</router-link> |
      <router-link to="/today">오늘</router-link> |
      <router-link to="/important">중요</router-link> |
    </nav>
    <h2>TodoPageView</h2>
    <router-view/>
  </div>
</template>

<script>
export default {
    name: 'TodoPageView'
}
</script>

<style>

</style>