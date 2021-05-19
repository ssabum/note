<template>
  <div>
    <h1>Video List</h1>
    <VideoListItem v-for="(video, idx) in $store.state.searchResult" :key="idx" :video="video"/>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  }
}
</script>

<style>

</style>