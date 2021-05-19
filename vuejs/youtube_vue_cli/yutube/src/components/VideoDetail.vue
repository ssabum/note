<template>
  <div v-if="video">
    <iframe :src="videoURI" frameborder=0></iframe>
    <h2>{{ video.snippet.title }}</h2>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object],
    }
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
    filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>