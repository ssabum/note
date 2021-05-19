<template>
  <div>
    <h1>This is Child</h1>
    <p>ChildData 👉 {{ childData }}</p>
    <input type="text" placeholder="Child" v-model="childData" @input="inputChildData">
    <p>AppData 👉 {{ appData }}</p>
    <p>ParentData 👉 {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  methods: {
    inputChildData: function () {
      // 데이터를 보낼때는 $emit 사용
      this.$emit('child-input', this.childData)
    }
  },
  props: {
    parentData: String,
    appData: String,
  },
  data: function () {
    return {
      childData: '',
    }
  }
}
</script>

<style>

</style>