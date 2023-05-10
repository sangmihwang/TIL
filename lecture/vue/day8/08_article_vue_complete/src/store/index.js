import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from "vuex-persistedstate";
// import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    article_id : 1,
    // 여기에 articles 데이터가 임시로 계속 쌓인다
    articles: [
      {
        id: 1,
        title: 'title1',
        content: 'content1',
        createdAt: new Date().getTime(),
      }
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article){
      state.articles.push(article)
      // 자동으로 article 번호 하나씩 늘어남
      state.article_id = state.article_id + 1
    },
    DELETE_ARTICLE(state, id){
      state.articles = state.articles.filter((article)=>{
        return !(article.id===id)
      })
    }
  },
  actions: {
    createArticle(context, payload){
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit('CREATE_ARTICLE', article) 
    }
  },
  modules: {
  }
})
