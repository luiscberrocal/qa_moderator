import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import i18n from './i18n'

import VueCookies from 'vue-cookies'

Vue.use(VueCookies)

Vue.use(Vuetify)
Vue.config.productionTip = false

new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
