<template>
  <div id="app">
    <h1 class="white--text display-3" >{{title}}</h1>
    <h2 class="white--text display-2">{{office}}</h2>
    <router-view/>
    <div>
      Version {{version}}
    </div>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        defaultTitle: 'Reunión de Comunicación Interna',
        defaultOffice: 'Oficina de Asuntos Importantes',
        defaultVersion: '?.?.?'
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
      },
      version() {
        if (this.$store.getters.appInfo){
          return this.$store.getters.appInfo.version;
        }else {
          return this.defaultVersion;
        }
      }
    },
    created() {
      this.$store.dispatch('GET_CURRENT_EVENT', 1);
      this.$store.dispatch('GET_APP_INFO');
    },
  }
</script>

<style lang="scss">
  body {
 //#53e3a6
background-color:  #68d4a6;
 }

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
