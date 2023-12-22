<template>
  <div id="app">
    <v-header />
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
    <v-footer v-if="showFooter" />
    <v-login v-if="showLogin" @loginSuccess="handleLoginSuccess" />
  </div>
</template>

<script>
import vHeader from "./components/header/v-header";
import vFooter from "./components/footer/v-footer";

export default {
  name: "App",
  components: {
    vHeader,
    vFooter,
  },
  computed: {
    showFooter() {
      return this.$route.name !== "login" && this.$route.name !== "signup";
    },
    showLogin() {
      return this.$route.name === "login";
    },
  },
  mounted() {
    this.$store.commit("initializeStore");
  },
};
</script>

<style></style>
