<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in todos" :key="idx">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
    <button @click="getTodos">Get Todos</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    getTodos: function () {
      axios.get(`${SERVER_URL}/todos/`)
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios.delete(`${SERVER_URL}/todos/${todo.id}/`)
        .then((res) => {
          console.log(res)
          // 1. findIndex(array helper methods)로 응답받은 아이디와 일치하는 요소의 index 찾기
          const targetTodoIdx = this.todos.findIndex((todo) => {
            return todo.id === res.data.id
          })
          // 2. 기존 배열(this.todos)에서 삭제한(target) todo를 삭제
          this.todos.splice(targetTodoIdx, 1)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) { // todo는 클릭한 todo를 의미
      const todoItem = {
        ...todo, // spread operator -> todoItem의 속성중에서 completed만 변경하려고 사용
        completed: !todo.completed
      }

      axios.put(`${SERVER_URL}/todos/${todo.id}/`, todoItem)
        .then((res) => {
          console.log(res)
          todo.completed = !todo.completed
        })
      },
    },
  created: function () {
    this.getTodos()
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>