import { createApp } from 'vue'
import App from './App.vue'
import Toast from './mixins/toast'
import store from './store'

// import TabNewItem from "./components/dashboard/tabs/TabNewItem.vue";

const app = createApp(App)

app.mixin(Toast)
app.use(store)

// app.component('TabNewItem', TabNewItem);

app.mount('#vue-app')

