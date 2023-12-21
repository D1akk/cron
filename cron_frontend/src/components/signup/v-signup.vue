<template>
  <div>
    <h3>Регистрация</h3>
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
      <div>
        <input v-model="password" type="password" placeholder="Пароль" />
        <small v-if="errors.password2">{{ errors.password2 }}</small>
      </div>
      <button type="submit" @click="login">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "vSignup",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: {
        username: "",
        password: "",
        password2: "",
        wrong_credentials: "",
      },
    };
  },
  // ...
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
      if (this.password && this.password2 && this.password != this.password2) {
        this.errors.password2 = "Пароли не совпадают";
      } else {
        this.password2 = "";
      }
      if(this.errors.username || this.errors.password || this.errors.password2){
        valid = false;
      }
      return valid;
    },
    submitForm() {
      if (this.isValidForm()) {
        const url = "/auth/users/";
        axios
          .post(url, {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            console.log(response.data);
            this.$router.push('/login')
            this.username = "";
            this.password = "";
            this.password2 = "";
          })
          .catch((error) => {
            if(error.response.data.username){
                this.errors.username = error.response.data.username.join('');
            }else{
                this.errors.username = '';
            }
                
          });
      }
    },
  },
  // ...
};
</script>

<style scoped>
/* Ваши стили для формы входа */
</style>
