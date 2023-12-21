<template>
  <div id="app">
    <v-header />
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
    <v-footer />
    <v-login v-if="showLogin" @loginSuccess="handleLoginSuccess" />
  </div>
</template>

<script>
import vHeader from "./components/header/v-header";
import vFooter from "./components/footer/v-footer";
import vLogin from "./components/login/v-login.vue";

export default {
  name: "App",
  components: {
    vHeader,
    vFooter,
    vLogin,
  },
  mounted(){
    this.$store.commit('initializeStore');
  }
};
</script>

<style></style>
