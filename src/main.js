import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import ElementPlus from 'element-plus'

const app = createApp(App)

app.config.globalProperties.$BackendUrl = 'http://192.168.1.2:5000'
// app.config.globalProperties.$BackendUrl = 'http://10.35.2.180:5000'
app.use(ElementPlus)
app.mount('#app')
