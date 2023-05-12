<template>
  <div>
    <h1>전체 영화 목록 페이지</h1>
    <div class="row col-md-4 float-left">
      <movie-card v-for="movie in movies" :key="movie.id" :movie="movie">
      </movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue"
import axios from "axios"

export default {
  name: "MovieView",
  components: {
    MovieCard,
  },
  data() {
    return {
      movies: [],
      apiKey: "c6d573e424ff520ecde3beacdc42ea62"
    }
  },
  mounted() {
    axios
      .get(`https://api.themoviedb.org/3/movie/top_rated?api_key=${this.apiKey}&language=ko-KR&page=1`)
      .then(response => {
        this.movies = response.data.results
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>
