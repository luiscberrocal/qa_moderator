import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL
})

//instance.defaults.headers.common['SOMETHING'] = 'something'
console.log('DELETE', process.env.VUE_APP_API_URL)
export default instance
