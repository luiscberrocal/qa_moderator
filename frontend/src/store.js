import Vue from 'vue'
import Vuex from 'vuex'
import axios from './django-auth'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    event: null,
    question: null
  },
  mutations: {
    setEvent(state, event) {
      state.event = event;
    },
    setQuestion(state, question) {
      state.question = question;
    }
  },
  actions: {
    'GET_CURRENT_EVENT'({commit}, eventId) {
      console.log('API URL', process.env.VUE_APP_API_URL);
      console.log('NODE Env', process.env.NODE_ENV);
      const url = `/events/api/v1/event/${eventId}/`;
      axios.get(url)
        .then((response) => {
          console.log('Event data', response.data);
          commit('setEvent', response.data);
        })
        .catch((error) => {
          console.log(error);
        })
      //commit('setEvent', dummyEvent);
    },
    'SEND_QUESTION'({commit, getters}, question) {
      const csrftoken = $cookies.get('csrftoken');
      //console.log('csrftoken', csrftoken)
      const headers = {headers: { 'X-CSRFToken': csrftoken}}
      const event = getters.event;
      const data = {question: question, event: event.id, moderator_num: 1}
      console.log('Question data', data, headers);
      const url = `/questions/api/v1/question/create/`;
      axios.post(url, data)
        .then((response) => {
          console.log('Question data', response.data);
          commit('setQuestion', response.data);
          this.$router.push('/thanks')
        })
        .catch((error) => {
          console.log('Post Question Error', error);
        })
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
