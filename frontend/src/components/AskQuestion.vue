<template>
  <v-container fluid grid-list-md text-xs-center fill-height>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <v-card>
          <v-toolbar dark color="teal">
            <v-toolbar-title>Question</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-layout row wrap>
              <v-container fluid grid-list-md>
                <v-textarea
                  name="input-7-1"
                  box
                  label="Label"
                  auto-grow
                  value=""
                ></v-textarea>
              </v-container>
            </v-layout>
          </v-card-text>
          <v-card-actions>
            <v-layout row>
              <v-flex xs12>
                <v-layout align-center justify-end row fill-height>
                  <v-btn right dark color="indigo"
                         @click.prevent="login">Submit
                  </v-btn>
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
        password: ''
      }
    },
    methods: {
      login() {
        const router = this.$router;
        const route = this.$route;
        //this.$store.dispatch('login', {username: this.username, password: this.password});
        this.$store.dispatch('login', {username: this.username, password: this.password});
      },
    },

    name: "AskQuestion"
  }
</script>

<style scoped>
</style>
