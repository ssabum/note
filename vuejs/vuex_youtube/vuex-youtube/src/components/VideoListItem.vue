<template>
    <li>
      <h1>Video List Item</h1>
      {{ video.snippet.title }}
    </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoTitle: {
      
    }
  }
}
</script>

<style>
ul{
  list-style:none;
}
</style>