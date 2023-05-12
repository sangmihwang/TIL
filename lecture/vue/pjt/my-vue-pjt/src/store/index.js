import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_KEY = 'c6d573e424ff520ecde3beacdc42ea62'
const TMDB_URL = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page=1&sort_by=vote_average.desc&without_genres=99,10755&vote_count.gte=200&api_key=${API_KEY}`

export default new Vuex.Store({
  state: {
    movies: [],
    weather: [],

  },
  getters: {
  },
  mutations: {
    SAVE_MOVIES(state, movies) {
      state.movies = movies
    },
  },
  actions: {
    // 재사용 가능성이 높으므로 action 에 작성
    getMovies(context) {
      axios.get(TMDB_URL)
      .then((response) => {
        context.commit('SAVE_MOVIES', response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
