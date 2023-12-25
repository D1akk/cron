<template>
  <div class="v-notes">
    <div v-for="(note, index) in notes" class="notes" :key="index">
      <div class="notes__top">
        <span class="notes__top-time">{{ note.time }}</span>
        <span class="notes__top-date">{{ note.date }}</span>
      </div>
      <span class="notes-span1">{{ note.type }}</span>
      <span class="notes-span2">{{ note.info }}</span>
      <div class="otmena">
        <span>Отменить запись</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'v-notes',
    components: {
    },
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
            ]
        }

    },
    methods:{
        fetchApointmentsList(){
            axios.defaults.headers['Authorization']=`Token ${this.$store.state.token}`;
            const url = '/appointment-list/';
            axios.get(url)
            .then(response => {
                console.log(response.data);
            })
            .catch(error=>{
                console.log(error);
            })
        }
    },
    mounted(){
        this.fetchApointmentsList();
    }
}
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
