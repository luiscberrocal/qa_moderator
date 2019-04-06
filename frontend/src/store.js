import Vue from 'vue'
import Vuex from 'vuex'

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
