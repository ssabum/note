<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="youtube-thumbnail-image">
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>
ul{
   list-style:none;
}
</style>