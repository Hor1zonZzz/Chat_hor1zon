<!-- 这个组件主要定义了一个标题，标题的内容是通过 ref 创建的响应式数据 title 来绑定的 -->

<template>
    <!-- 以下代码使得字体一个一个显示出来，再一起消失，再一个一个显示出来，再一起消失往复动效 -->
    <h1 class="enTitle">{{ head_title }}</h1>
    <!-- 循环 -->
    <div class="text-animation">
        <span class="zhTitle" v-for="(char, index) in text" :key="index" :style="{ animationDelay: `${index * 0.5}s` }" >{{ char }}</span>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    setup() {
        const head_title = ref('Open Your Horizon');
        const showContent = ref(false);

        return {
            head_title,
            showContent,
            text: '目光所及，皆是原野'
        };
    }
};
</script>

<style>
.enTitle {
    padding-top: 5%;
    padding-bottom: 3%;
    text-align: center;
    font-size: 42px;
    color: #005c18;
    font-family: Arial, Helvetica, sans-serif;
}

.zhTitle {
    font-size: 23px;
    color: #025735;
    font-family: 'Courier New', Courier, monospace;
}

.text-animation {
    text-align: center;
    overflow: hidden; /* 确保动画过程中不会影响其他元素 */
    white-space: nowrap; /* 防止文字换行 */
}

.text-animation span {
  opacity: 0; /* 初始状态为透明 */
  animation: reveal 1s ease-in-out forwards; /* 应用动画 */
}

@keyframes reveal {
    to {
        opacity: 1;
    }
}
</style>