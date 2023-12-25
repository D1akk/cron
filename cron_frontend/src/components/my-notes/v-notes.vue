<template>
  <div class="v-notes">
    <div v-for="(note, index) in notes" class="notes" :key="index">
      <div class="notes__top">
        <span class="notes__top-time">{{ note.time }}</span>
        <span class="notes__top-date">{{ note.date }}</span>
      </div>
      <span class="notes-span1">{{ note.clinicTitle }}</span>
      <span class="notes-span3">{{ note.clinicLocation }}</span>
      
      <span class="notes-span2">Вам напомнят за 30 минут до приема</span>
      <div class="otmena">
        <span>Отменить запись</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "v-notes",
  components: {},
  data() {
    return {
      notes: [
        // {
        //     time: '13:00',
        //     date: '16.09.2023',
        //     type: 'Запись к терапевту',
        //     info: 'Вам напомнят за 30 минут до приема'
        // },
        // {
        //     time: '13:00',
        //     date: '16.09.2023',
        //     type: 'Запись к терапевту',
        //     info: 'Вам напомнят за 30 минут до приема'
        // },
        // {
        //     time: '13:00',
        //     date: '16.09.2023',
        //     type: 'Запись к терапевту',
        //     info: 'Вам напомнят за 30 минут до приема'
        // },
        // {
        //     time: '13:00',
        //     date: '16.09.2023',
        //     type: 'Запись к терапевту',
        //     info: 'Вам напомнят за 30 минут до приема'
        // }
      ],
      clinics: {},
    };
  },
  methods: {
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
.v-notes {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.notes {
  background-color: var(--white);
  padding: 20px 16px;
  border-radius: 20px;
}

.notes__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.notes__top-time {
  font-size: 30px;
  font-weight: 500;
  letter-spacing: -1.2px;
}

.notes__top-date {
  color: var(--grey);
  line-height: 150%;
  letter-spacing: -0.176px;
  font-size: 16px;
}

.notes-span1 {
  display: block;
  margin-bottom: 10px;
  font-size: 16px;
}

.notes-span2 {
  color: var(--grey);
  font-size: 16px;
  margin-bottom: 20px;
  display: block;
}

.notes-span3 {
  font-size: 12px;
  margin-bottom: 20px;
  display: block;
}


.notes-span4 {
  font-size: 12px;
  margin-bottom: 20px;
  display: block;
}


.otmena {
  border-top: 1px solid var(--light-grey);
  padding-top: 20px;
  font-size: 16px;
  color: #ff2e2e;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
