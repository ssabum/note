import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_KEY = process.env.VUE_ADD_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: { // 데이터
    searchResult: null,
  },
  mutations: { // 데이터를 저장할 때, 동기만 가능
    ADD_SEARCH_RESULT: function (state, items) {
      state.searchResult = items
    }
  },
  actions: { // methods 같은 것
    onSearch: function ({ commit }, query) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: query
      }

      axios({
        url: API_URL,
        method: 'get',
        params,
      }).then(res => {
        commit('ADD_SEARCH_RESULT', res.data.items)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: { // store가 너무 커지면 분리할 때 사용
  },
  getters: { // computed 역할
  }
})
