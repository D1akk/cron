<template>
  <div>
    <form @submit.prevent="submitForm">
      <div v-if="errors.wrong_credentials">
        <small>{{ errors.wrong_credentials }}</small>
      </div>
      <div>
        <input v-model="username" placeholder="Электронная почта" />
        <small v-if="errors.username">{{ errors.username }}</small>
      </div>
      <div>
        <input v-model="password" type="password" placeholder="Пароль" />
        <small v-if="errors.password">{{ errors.password }}</small>
      </div>
      <button type="submit" @click="login">Войти</button>
      <div>
        <p>
          <router-link to="/signup">Регистрация</router-link>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "vLogin",
  data() {
    return {
      username: "",
      password: "",
      errors: {
        username: "",
        password: "",
        wrong_credentials: "",
      },
    };
  },
  methods: {
    isValidForm() {
      let valid = true;
      if (!this.username) {
        this.errors.username = "Поле не может быть пустым";
        valid = false;
      } else {
        this.errors.username = "";
      }
      if (!this.password) {
        this.errors.password = "Поле не может быть пустым";
        valid = false;
      } else {
        this.errors.password = "";
      }
      return valid;
    },
    submitForm() {
      if (this.isValidForm()) {
        const url = "/login/";
        axios
          .post(url, {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            // console.log(response.data);
            this.$store.commit("setToken", response.data);
            this.username = "";
            this.password = "";
            this.$router.push('/');
          })
          .catch((error) => {
            if (error.response.data.non_field_errors) {
              this.errors.wrong_credentials =
                error.response.data.non_field_errors.join("");
            } else {
              this.errors.wrong_credentials = "";
            }
          });
      }
    },
  },
};
</script>

<style scoped>
</style>
