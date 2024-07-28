<template>
    <!-- 下面模块是聊天页面布局 -->
    <div class="common-layout">
      <!-- 按钮跳转到个人博客网站 -->
      <el-button round style="background-color: transparent;" @click="goToprofile">我的个人主页</el-button>
    <el-container>
      <!-- 头部标题 -->
      <el-header>
        <Head_title />
      </el-header>
      <el-main>
        <div class="mainContainer">
          <ChatWindow />
        </div>
      </el-main>
    </el-container>
  </div>
  </template>
  
<script>
import ChatWindow from './ChatWindow.vue'
import Head_title from './Head_title.vue';
  export default {
    components: {
      ChatWindow,
      Head_title
    },
    methods: {
      goToprofile() {
        this.$router.push('/about')
      }
    }
  }
  </script>
  
<style>
  .mainContainer {
  display: flex;
  justify-content: center;
}

    .el-header {
  height: fit-content;
}

  .el-mian {
  height: fit-content;
}



#title {
  width: fit-content;
  height: fit-content;
  padding-top: 20%;
}
</style>