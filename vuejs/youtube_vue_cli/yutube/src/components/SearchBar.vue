<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text" placeholder="검색어">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style>

</style>