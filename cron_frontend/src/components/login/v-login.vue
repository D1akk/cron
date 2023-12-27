<template>
  <div class="v-home">
    <div class="home-top">
      <div class="home__title-item">
        <h1 class="home-title">CRON<span>.</span></h1>
      </div>
      <p class="login-subtitle">Для входа введите логин и пароль</p>
    </div>
  </div>
  <form @submit.prevent="submitForm" class="form">
    <div v-if="errors.wrong_credentials">
      <small>{{ errors.wrong_credentials }}</small>
    </div>
    <div class="input-container">
      Логин
      <input v-model="username" placeholder="Введите ФИО" />
      <small v-if="errors.username">{{ errors.username }}</small>
    </div>
    <div class="input-container">
      Пароль
      <input v-model="password" type="password" placeholder="Введите пароль" />
      <small v-if="errors.password">{{ errors.password }}</small>
    </div>
    <button type="submit" @click="login" class="submit">Войти</button>
    <div>
      <p>
        <router-link to="/signup">Регистрация</router-link>
      </p>
    </div>
  </form>
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
            this.$router.push("/");
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

<style>
.v-home {
  display: grid;
  gap: 10px;
}

.push {
  margin-top: 8px;
}

.home-title {
  font-size: 40px;
  font-weight: 500;
  line-height: normal;
  letter-spacing: -1.6px;
}

.home-title span {
  color: var(--orange);
}

.home__title-item {
  display: flex;
  margin-bottom: 4px;
}

.home-top {
  background-color: var(--white);
  padding-top: 30px;
  padding-bottom: 20px;
  border-radius: 0px 0px 20px 20px;
}

.home-top-p {
  font-size: 16px;
  line-height: 150%;
  letter-spacing: -0.176px;
  color: var(--grey);
  margin-bottom: 20px;
}

.home-top__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.home-top__box {
  height: 106px;
  width: 100%;
  border-radius: 20px;
  color: var(--white);
  position: relative;
}

.home-top__box.blue {
  background-color: var(--blue);
}

.home-top__box.orange {
  background-color: var(--orange);
}

.home-top__box__flex {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
}

.home-top__box__flex {
  font-size: 12px;
}

.home-top__box-bottom-spam {
  position: absolute;
  bottom: 16px;
  left: 16px;
  font-size: 16px;
}

.home__mid {
  background-color: white;
  border-radius: 20px;
  padding: 20px 0;
}

.home__mid-p {
  font-size: 16px;
  line-height: 150%;
  letter-spacing: -0.176px;
  margin-bottom: 16px;
}

.home__mid__grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 16px;
}

.home__mid__cart {
  background-color: var(--light-grey);
  border-radius: 10px;
  color: var(--grey);
  padding: 14px;
  position: relative;
  display: flex;
  align-items: flex-start;
}

.home__mid__cart.active {
  background-color: var(--blue);
  color: var(--white);
}

.home__mid__cart-big {
  font-size: 16px;
}

.home__mid__cart-small {
  font-size: 10px;
  margin-top: 1px;
}

.home__bottom {
  background-color: var(--white);
  border-radius: 20px 20px 0 0;
  padding: 20px 0 24px;
  margin-bottom: 67px;
}

.home__bottom__cart {
  border-radius: 20px;
  border: 1px solid #efefef;
  background: var(--light-grey);
  margin-bottom: 10px;
}

.home__bottom__cart svg {
  margin: 10px 10px 43px;
}

.home__bottom__cart p {
  margin: 0px 16px 5px;
}

.home__bottom__cart span {
  display: block;
  margin: 0px 16px 11px;
  font-size: 12px;
  color: var(--grey);
}

.login-subtitle {
  display: block;
  font-size: 12px;
  color: var(--grey);
}

.aksii {
  background: linear-gradient(90deg, #5071e6 0%, #8b55e9 98.14%);
}

.home__bottom__cart.aksii,
.home__bottom__cart.aksii span {
  color: white;
}

.form {
  /* background-color: #fff; */
  display: block;
  padding: 1rem;
  max-width: 350px;
  /* border-radius: 0.5rem; */
  /* box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); */
}

.form-title {
  font-size: 1.25rem;
  line-height: 1.75rem;
  font-weight: 600;
  text-align: center;
  color: #000;
}

.input-container {
  position: relative;
}

.input-container input,
.form button {
  outline: none;
  border: 1px solid #e5e7eb;
  margin: 8px 0;
  width: 300px;
}

.input-container input {
  background-color: #fff;
  padding: 1rem;
  padding-right: 3rem;
  font-size: 0.875rem;
  line-height: 1.25rem;
  width: 300px;
  border-radius: 0.5rem;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}

.submit {
  display: block;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  padding-left: 1.25rem;
  padding-right: 1.25rem;
  background-color: #4b68d0;
  color: #ffffff;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-weight: 500;
  width: 100%;
  border-radius: 0.5rem;
  text-transform: uppercase;
}

.signup-link {
  color: #6b7280;
  font-size: 0.875rem;
  line-height: 1.25rem;
  text-align: center;
}

.signup-link a {
  text-decoration: underline;
}
</style>
