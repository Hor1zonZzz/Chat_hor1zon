<template>
    <div>
      <button @click="increment">Count is: {{ count }}</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  // 定义一个响应式变量 count
  const count = ref(0)
  
  // 定义一个方法来增加 count 的值
  function increment() {
    count.value++
  }
  </script>
  
  <style scoped>
  button {
    font-weight: bold;
  }
  </style>