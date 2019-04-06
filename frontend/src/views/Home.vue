<template>
  <div class="home">
   <ask-question></ask-question>
  </div>
</template>

<script>
// @ is an alias to /src
import AskQuestion from '@/components/AskQuestion.vue'

export default {
  name: 'home',
  components: {
    AskQuestion
  }
}
</script>
