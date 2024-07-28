import { createApp } from 'vue'
import './global.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import './assets/styles.css'
// 创建一个 Vue 应用实例
// createApp(App).mount('#app')

const app = createApp(App)

// 
app.use(ElementPlus)
app.use(router).mount('#app')