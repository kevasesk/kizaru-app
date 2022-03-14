import { createApp } from 'vue'
import App from './App.vue'
import Toast from './mixins/toast.js'

const app = createApp(App)

app.mixin(Toast)
app.mount('#vue-app')

