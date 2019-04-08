<template>
  <div class="home">
    <h1 class="indigo--text display-4 py-4 font-weight-regular font-italic ">{{ $t('thanks') }}!!</h1>
    <v-btn dark color="indigo" @click="askQuestion">Ask another question</v-btn>
    <v-snackbar v-model="snackbar" color="red" :timeout="timeout">{{message}}
      <v-btn
        dark
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  // @ is an alias to /src
  import AskQuestion from '@/components/AskQuestion.vue'
  import {mapGetters} from 'vuex'

  export default {
    name: 'ThankYou',
    data() {
      return {
        message: '',
        timeout: 7000,
        displaySnack: false
      }
    },
    components: {
      AskQuestion
    },
    computed: {
      ...mapGetters([
        'error',
      ]),
      snackbar: {
        get() {
          if (this.error) {
            console.log('computed ERROR');
            const errorMessage = this.$store.getters.error.response.statusText;
            const status = this.$store.getters.error.response.status;
            this.message = `There was a ${status} error ${errorMessage}!!. Please contact your support personel.`
            //this.snackbar = true;
            return true
          } else {
            console.log('computed NO ERROR');
            return false
          }
        },
        set(value) {
          this.displaySnack = value;
        }
      }
    },
    methods: {
      askQuestion() {
        this.$router.push({name: 'home'});
      }
    },
    created() {
      if (this.$store.getters.error) {
        console.log('ERROR');
        const errorMessage = this.$store.getters.error.response.statusText;
        const status = this.$store.getters.error.response.status;
        this.message = `There was a ${status} error ${errorMessage}!!. Please contact your support personel.`
        this.snackbar = true;
      } else {
        console.log('NO ERROR');
      }
    },
    destroyed() {
      console.log('Clearing error')
      this.$store.dispatch('CLEAR_ERROR');
    }
  }
</script>
