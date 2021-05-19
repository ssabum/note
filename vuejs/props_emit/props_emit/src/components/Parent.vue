<template>
  <div>
    <h1>This ih Parent</h1>
    <p>ParentData 👉 {{ parentData }}</p>
    <input type="text" placeholder="Parent" v-model="parentData" @input="inputParentData">
    <p>AppData 👉 {{ appData }}</p>
    <p>ChildData 👉 {{ childData }}</p>
    <Child :parentData="parentData" :appData="appData" @child-input="inputChild"></Child>

  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  methods: {
    inputChild: function (data) {
      // console.log('용가뤼')
      this.childData = data
      this.$emit('child-input', this.childData)
    },
    inputParentData: function () {
      this.$emit('parent-input', this.parentData)
    }
  },
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  components: {
    Child,
  },
  props: {
    appData: String, 
  }
}
</script>

<style>

</style>