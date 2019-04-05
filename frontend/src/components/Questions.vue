<template>
  <v-container fluid grid-list-md text-xs-center fill-height>
    <v-layout row wrap align-center>
      <v-flex xs12 md6 offset-md3>
        <v-card>
          <v-toolbar dark color="teal">
            <v-toolbar-title>QA </v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-layout row wrap>
              <v-flex xs12>
                <v-text-field
                  label="User name"
                  prepend-icon="person"
                  v-model="username"
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Password"
                  prepend-icon="lock"
                  type="password"
                  v-model="password"
                ></v-text-field>
              </v-flex>
            </v-layout>
          </v-card-text>
          <v-card-actions>
            <v-layout row>
              <v-flex xs12>
                <v-layout align-center justify-end row fill-height>
                  <v-btn right dark color="indigo"
                         @click.prevent="login">Login
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
        username: '',
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
    name: "Login"
  }
</script>

<style scoped>
</style>
