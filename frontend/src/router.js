import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import ThankYou from './views/ThankYou.vue'
import EventQuestion from './views/EventQuestion.vue'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/event/:id',
      name: 'event',
      component: EventQuestion
    },
    {
      path: '/thanks',
      name: 'thanks',
      component: ThankYou
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
