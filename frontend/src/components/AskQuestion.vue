<template>
  <v-container fluid grid-list-md text-xs-center fill-height>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <v-card>
          <v-toolbar dark color="teal">
            <v-toolbar-title>{{ $t('question') }}</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-layout row wrap>
              <v-container fluid grid-list-md>

                <v-textarea
                  name="input-7-1"
                  box
                  label=""
                  auto-grow
                  v-model="question"
                ></v-textarea>
              </v-container>
            </v-layout>
          </v-card-text>
          <v-card-actions>
            <v-layout row>
              <v-flex xs12>
                <v-layout align-center justify-end row fill-height>
                  <v-btn right color="indigo"
                         class="white--text"
                         :disabled="readyToSend"
                         @click.prevent="sendQuestion">{{ $t('send_question') }}</v-btn>
                </v-layout>
              </v-flex>
            </v-layout>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import {mapActions} from 'vuex';

  export default {
    data() {
      return {
        event: null,
        question: '',
        readyToSend: true
      }
    },
    watch:{
      question(val){
        if(val.length > 3){
          this.readyToSend = false;
        }else {
          this.readyToSend = true;
        }
      }
    },
    methods: {
      sendQuestion() {
        const router = this.$router;
        const route = this.$route;
        this.$store.dispatch('SEND_QUESTION', this.question)
        this.$router.push('/thanks')
      },
      ready(){
        return false;
      }
    },

    name: "AskQuestion"
  }
</script>

<style scoped>
</style>
