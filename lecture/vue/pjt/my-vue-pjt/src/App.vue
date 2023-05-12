<template>
  <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">SSAFY</b-navbar-brand>
      <b-navbar-nav class="justify-content-end">
        <router-link to="/movies">Movie</router-link> |
        <router-link to="/random">Random</router-link>|
        <router-link to="/watch-list">WatchList</router-link>
        </b-navbar-nav>
    </b-navbar>
  <router-view/>
</div>

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
