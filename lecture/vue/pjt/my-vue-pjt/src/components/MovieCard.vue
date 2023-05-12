<template>
  <div>
    <div class="card mb-4">
          <img class="card-img-top" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.overview }}</p>
            
          </div>
        </div>
  </div>
</template>

<script>
export default {
    name: "MovieCard",
    props: {
            movie: Object
        }
}
</script>

<style>

</style>