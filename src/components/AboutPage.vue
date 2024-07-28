<template>
    <el-carousel :interval="4000" type="card" height="400px">
      <el-carousel-item v-for="item in urlList" :key="item.value">
        <h3 text="2xl" justify="center">
          <el-image
            :src="item.value"
            fit="cover"
            width="100%"
            height="100%"
          ></el-image>
        </h3>
      </el-carousel-item>
    </el-carousel>
  </template>
  
  <script>
  export default {
    data() {
      return {
        urlList: [
          { value: require('@/assets/1.webp') }, // 使用 require 引入图片
          { value: require('@/assets/2.webp') },
          { value: require('@/assets/3.webp') },
          { value: require('@/assets/4.webp') },
          { value: require('@/assets/5.webp') }

        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
  }
  </style>
  