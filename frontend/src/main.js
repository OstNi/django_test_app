import { createApp } from 'vue'
import App from './App.vue'

import router from './router'

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


import axios from 'axios'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const app = createApp(App)
app.use(router).use(vuetify).mount('#app')
