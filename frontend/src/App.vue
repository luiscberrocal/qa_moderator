<template>
  <div id="app">
    <h1>{{title}}</h1>
    <h2>{{office}}</h2>
    <div id="nav">
      <router-link to="/">Home</router-link>
      |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        defaultTitle: 'Reunión de Comunicación Interna',
        defaultOffice: 'Oficina de Asuntos Importantes'
      }
    },
    computed: {
      title() {
        if (this.$store.getters.event) {
          return this.$store.getters.event.name || this.defaultTitle;
        }
      },
      office() {
         if (this.$store.getters.event) {
           return this.$store.getters.event.office_name || this.defaultOffice;
         }
      }
    },
    created() {
      this.$store.dispatch('GET_CURRENT_EVENT', 1);
    },
  }
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;
    a {
      font-weight: bold;
      color: #2c3e50;
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>
