<template>
  <div id="app">
    <h1>This is App</h1>
    <p>AppData 👉 {{ appData }}</p>
    <input type="text" placeholder="App" v-model="appData">
    <p>ParentData 👉 {{ parentData }}</p>
    <p>ChildData 👉 {{ childData }}</p>
    <Parent :appData="appData" @child-input="inputChild" @parent-input="inputParent"></Parent>
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name: 'App',
  methods: {
    inputChild: function (data) {
      this.childData = data
    },
    inputParent: function (data) {
      this.parentData = data
    }
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  components: {
    Parent,
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
