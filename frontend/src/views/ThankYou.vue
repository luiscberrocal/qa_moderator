<template>
  <div class="home">
   <h1>Thanks</h1>
    <v-btn dark color="indigo" @click="askQuestion">Ask another question</v-btn>
  </div>
</template>

<script>
// @ is an alias to /src
import AskQuestion from '@/components/AskQuestion.vue'

export default {
  name: 'ThankYou',
  components: {
    AskQuestion
  },
  methods: {
    askQuestion() {
      this.$router.push({name: 'home'});
    }
  },
}
</script>
