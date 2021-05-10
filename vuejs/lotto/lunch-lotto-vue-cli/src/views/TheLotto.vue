<template>
  <div>
    <h1>🙏로또 번호 추천</h1>
    <button @click='getLuckNums'>Pick Lotto Numbers</button>
    <p>로또 번호 {{ $route.params.lottoNum }}개 추천</p>
    <p>오늘의 추천 로또 번호👇</p>
    <ul>
      <li v-for='(num, idx) in selectedLuckyNums' :key='idx'>{{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function() {
    return {
      selectedLuckyNums: []
    }
  },
  methods: {
    getLuckNums: function() {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLuckyNums = _.sortBy(this.sampleNums)
    }
  }
}
</script>

<style>
ul{
   list-style:none;
   }
</style>