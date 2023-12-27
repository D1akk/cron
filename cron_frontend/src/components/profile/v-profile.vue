<template>
  <div class="v-profile">
    <div class="profile-top">
      <div class="container">
        <div class="profile__title-item">
          <h1 class="profile-title">Профиль</h1>
          <div class="push">
            <svg width="40" height="40">
              <use xlink:href="../../assets/img/sprite.svg#push"></use>
            </svg>
          </div>
        </div>
        <p class="profile-top-p">Мои данные</p>
      </div>
    </div>
    <div class="profile-mid">
      <span class="profile-mid-greu">ФИО</span>
      <span class="profile-mid-black">Иванов Иван иванович</span>
      <span class="profile-mid-greu">Телефон</span>
      <span class="profile-mid-black">+7 (999)-123-45-67</span>
      <div class="profile-mid-redactor">Редактировать профиль</div>
      <div class="profile-mid-exit">
        <a @click="logout">Выйти из аккаунта</a>
      </div>
    </div>
    <div class="profile-bottom">
      <div href="#" class="profile-top__box">
        <div class="profile-top__box__flex">
          <svg width="32" height="32">
            <use xlink:href="../../assets/img/sprite.svg#history"></use>
          </svg>
        </div>
        <span class="profile-top__box-bottom-spam">История записей</span>
        <span class="profile-top__box-bottom-spam02"
          >Список ваших записей за все время</span
        >
      </div>
      <div href="#" class="profile-top__box">
        <div class="profile-top__box__flex">
          <svg width="32" height="32">
            <use xlink:href="../../assets/img/sprite.svg#shit"></use>
          </svg>
        </div>
        <span class="profile-top__box-bottom-spam">О приложении</span>
        <span class="profile-top__box-bottom-spam02"
          >Все о приложении и пользовательском соглашении</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "v-profile",
  components: {},
  data() {
    return {};
  },
  methods: {
    logout() {
      this.$store.commit("removeToken");
      this.$router.push("/login");
    },
    
    fetchApointmentsList() {
      // console.log("User ID:", this.$store.state.user_id);
      // console.log("Token:", this.$store.state.token);
      if (!this.$store.state.user_id) {
        return;
      }
      axios.defaults.headers[
        "Authorization"
      ] = `Token ${this.$store.state.token}`;
      const url = "/appointment-list/";
      // const user_id = this.$store.state.user_id;
      axios
        .get(url)
        .then((response) => {
          // Фильтрация записей для текущего пользователя
          const filteredNotes = response.data.filter(
            (note) => note.patient == this.$store.state.user_id
          );

          // Получение названия клиники для каждой записи
          const promises = filteredNotes.map((note) =>
            axios.get(`/clinic-details/${note.clinic}/`)
          );

          // Обработка всех запросов
          axios.all(promises).then((clinicResponses) => {
            clinicResponses.forEach((clinicResponse, index) => {
              filteredNotes[index].clinicTitle = clinicResponse.data.title;
              filteredNotes[index].clinicLocation = clinicResponse.data.location;
            });

            // Обновление состояния компонента
            this.notes = filteredNotes;
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.fetchApointmentsList();
  },
};
</script>
<style>
.v-profile {
  display: block;
  margin-bottom: 48px;
}

.profile-top {
  padding: 30px 0 20px;
  background-color: var(--white);
  border-radius: 0 0 20px 20px;
  margin-bottom: 20px;
}

.profile__title-item {
  display: flex;
  justify-content: space-between;
}

.profile-title {
  font-size: 40px;
  font-weight: 500;
  letter-spacing: -1.6px;
  margin-bottom: 4px;
}

.profile-top-p {
  color: var(--grey);
  font-size: 16px;
  line-height: 150%; /* 24px */
  letter-spacing: -0.176px;
}

.profile-mid {
  background-color: var(--white);
  padding: 18px 16px 20px;
  border-radius: 20px;
}

.profile-mid-greu {
  font-size: 12px;
  color: var(--grey);
  letter-spacing: -0.48px;
  margin-bottom: 4px;
  display: block;
}

.profile-mid-black {
  display: block;
  line-height: 150%; /* 24px */
  letter-spacing: -0.176px;
  padding-bottom: 20px;
}

.profile-mid-redactor {
  color: var(--blue);
  line-height: 150%; /* 24px */
  letter-spacing: -0.176px;
  padding: 20px 0;
  border-top: 1px solid var(--light-grey);
  border-bottom: 1px solid var(--light-grey);
}

.profile-mid-exit{
  color: #ff2e2e;
  line-height: 150%; /* 24px */
  letter-spacing: -0.176px;
  padding: 20px 0 0;
}

.profile-mid-exit a{
  color: #ff2e2e
}

.profile-bottom {
  display: block;
  margin-top: 10px;
  padding: 20px 16px 52px;
  background-color: var(--white);
  border-radius: 20px 20px;
}

.profile-top__box {
  padding: 10px 10px 11px;
  border-radius: 20px;
  background-color: #f4f4f8;
  margin-bottom: 10px;
}

.profile-top__box__flex {
  margin-bottom: 43px;
}

.profile-top__box-bottom-spam {
  display: block;
  line-height: 150%; /* 24px */
  letter-spacing: -0.176px;
  margin: 0 16px 5px;
}

.profile-top__box-bottom-spam02 {
  display: block;
  font-size: 12px;
  color: var(--grey);
  margin: 0 16px 11px;
}
</style>
