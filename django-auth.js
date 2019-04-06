import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.API_URL
})

//instance.defaults.headers.common['SOMETHING'] = 'something'

export default instance
