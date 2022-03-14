import { createApp } from 'vue'
import App from './App.vue'
import Toast from './mixins/toast'
import store from './store'

const app = createApp(App)

app.mixin(Toast)
app.use(store)
app.mount('#vue-app')

