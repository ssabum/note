<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
      <SearchBar @input-search="onInputSearch"></SearchBar>
      <br>
      <VideoDetail :video="selectedVideo"/>
      <br>
      <VideoList :videos="videos" @select-video="onVideoSelect"/>
  </div>
</template>

<script>
import axios from 'axios'

import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const API_KEY = 'AIzaSyApC8UnI70h-gfhT6WfU8_ygE15sKt8a6E'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onInputSearch: function (inputText) {
      // console.log(inputText)
      this.inputValue = inputText
      // part(필수), key(필수), q(검색어), type(video)
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios.get(API_URL, {
        params,
      })
      .then((res) => {
        console.log(res)
        // console.log(res.data.items)
        this.videos = res.data.items
        if (!this.selectedVideo) {
          this.selectedVideo = this.videos[0]
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    }
  },
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
