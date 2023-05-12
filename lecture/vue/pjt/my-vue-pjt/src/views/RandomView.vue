<template>
  <div>
    <h1>랜덤 영화 추천</h1>
    <div class="card mb-4 col-md-4">
      <img class="card-img-top" :src="`https://image.tmdb.org/t/p/original/${selectedMovie.poster_path}`" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title">{{ selectedMovie.title }}</h5>
        <p class="card-text">{{ selectedMovie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RandomView",
  data() {
    return {
      movies: [],
      selectedMovie: {},
      apiKey: "c6d573e424ff520ecde3beacdc42ea62"
    };
  },
  mounted() {
    axios
      .get(`https://api.themoviedb.org/3/movie/top_rated?api_key=${this.apiKey}&language=ko-KR&page=1`)
      .then(response => {
        this.movies = response.data.results
        this.selectRandomMovie()
      })
      .catch(error => {
        console.log(error);
      })
  },
  methods: {
    selectRandomMovie() {
      const randomIndex = Math.floor(Math.random() * this.movies.length)
      this.selectedMovie = this.movies[randomIndex]
    }
  }
}
</script>
