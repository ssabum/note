<template>
  <div>
    <input type="text" @keyup.enter="onSearch" v-model="query">
    <button @click="onSearch" style="margin: 0 0 0 1rem">Search</button>
  </div>
</template>

<script>
export default { // 비디오 검색을 위한 컴포넌트
  name: 'VideoSearchBar',
  data: function () { // 컴포넌트 안에는 데이터를 function 형태
    return {
      query: '',
    }
  },
  mehtods: {
    onSearch: function () {
      // console.log(`${this.query}`)
      this.$store.dispatch('onSearch', this.query)
    }
  }
}
</script>

<style>

</style>