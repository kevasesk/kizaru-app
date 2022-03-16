import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

import Toast from './mixins/toast'
import Timeout from './mixins/timeout'

// import TabNewItem from "./components/dashboard/tabs/TabNewItem.vue";

const app = createApp(App)

app.mixin(Toast)
app.mixin(Timeout)

app.use(store)

app.mount('#vue-app')

