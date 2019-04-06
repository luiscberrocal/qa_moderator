import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.API_URL
})

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    event: null,
    question: null
  },
  mutations: {
    setEvent(state, event){
      state.event = event;
    },
    setQuestion(state, question){
      state.question = question;
    }
  },
  actions: {
    'GET_CURRENT_EVENT'({commit}, eventId){
      let dummyEvent = {name: 'RCI AC', id: 1};
      console.log('API URL', process.env.VUE_APP_API_URL);
      console.log('NODE Env', process.env.NODE_ENV);
      commit('setEvent', dummyEvent);
    }
  },
  getters: {
    event: state => {
      return state.event;
    },
    question: state => {
      return state.question;
    }
  }
})
