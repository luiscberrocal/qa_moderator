import Vue from 'vue'
import Vuex from 'vuex'
import axios from '../django-auth'


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    event: null,
    question: null,
    appInfo: null,
    error: null
  },
  mutations: {
    setEvent(state, event) {
      state.event = event;
    },
    setQuestion(state, question) {
      state.question = question;
    },
    setAppInfo(state, appInfo) {
      state.appInfo = appInfo;
    },
    setError(state, error) {
      state.error = error;
    },
    clearError(state) {
      state.error = null;
    },

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
    'SEND_QUESTION'({commit, getters, dispatch}, question) {
      const csrftoken = $cookies.get('csrftoken');
      console.log('csrftoken', csrftoken);
      const headers = {headers: {'X-CSRFToken': csrftoken}};
      //const headers = {headers: {"Authorization": `Bearer ${JWTToken}`, 'Content-Type': 'multipart/form-data'}}
      const event = getters.event;
      const data = {question: question, event: event.id, moderator_num: 1};
      console.log('Question data to POST', data, headers);
      const url = `/questions/api/v1/question/create/`;
      axios.post(url, data, headers)
        .then((response) => {
          console.log('Question data retrieved', response.data);
          commit('setQuestion', response.data);
        })
        .catch((error) => {
          console.log('Post Question Error', error);
          dispatch('SET_ERROR', error);
        })
    },
    'GET_APP_INFO'({commit}) {
      const url = `/core/api/v1/app-info/`;
      axios.get(url)
        .then((response) => {
          console.log('App Info', response.data);
          commit('setAppInfo', response.data);
        })
        .catch((error) => {
          console.log(error);
        })
    },
    'SET_ERROR'({commit}, error) {
      console.log('Error to SET', error);
      commit('setError', error)
    },
    'CLEAR_ERROR'({commit}) {
      //Clears the error state
      commit('clearError')
    }
  },
  getters: {
    event: state => {
      return state.event;
    },
    question: state => {
      return state.question;
    },
    appInfo: state => {
      return state.appInfo;
    },
    error: state => {
      return state.error;
    }
  }
})
