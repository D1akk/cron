<template>
  <div class="v-home">
    <div class="home-top">
      <div class="container">
        <div class="home__title-item">
          <h1 class="home-title">Приветствуем в CRON<span>.</span></h1>
          <div class="push">
            <svg width="40" height="40">
              <use xlink:href="../../assets/img/sprite.svg#push"></use>
            </svg>
          </div>
        </div>
        <p class="home-top-p">
          Мгновенная запись на прием<br />к стоматологу без звонка
        </p>
        <div class="home-top__grid">
          <a href="#" @click="showModalDate" class="home-top__box blue">
            <div class="home-top__box__flex">
              <svg width="32" height="32">
                <use xlink:href="../../assets/img/sprite.svg#calendar"></use>
              </svg>
              <span
                >{{ selectedDate.day }}.{{ selectedDate.month }}.{{
                  selectedDate.year
                }}</span
              >
            </div>
            <span class="home-top__box-bottom-spam"
              >{{ selectedDate.day }}.{{ selectedDate.month }}.{{
                selectedDate.year
              }}</span
            >
            <!-- <span class="home-top__box-bottom-spam">Сегодня</span> -->
          </a>
          <SelectData
            @selected-date="updateSelectedDate"
            ref="modalDate"
          ></SelectData>
          <a href="#" @click="showModalUsluga" class="home-top__box orange">
            <div class="home-top__box__flex">
              <svg width="32" height="32">
                <use xlink:href="../../assets/img/sprite.svg#apteka"></use>
              </svg>
            </div>
            <span class="home-top__box-bottom-spam">{{ selectedUsluga }}</span>
            <span class="home-top__box-bottom-spam">Выбрать услугу</span>
          </a>
          <SelectUsluga
            :parentUslugas="uslugas"
            v-model="selectedUsluga"
            @selected-usluga="handleSelectedUsluga"
            ref="modalUsluga"
          ></SelectUsluga>
        </div>
      </div>
    </div>
    <div class="home__mid">
      <div class="container">
        <p class="home__mid-p">Свободные окна к специалистам в этот день</p>
        <div class="home__mid__grid">
          <label
            v-for="(time, index) in times"
            :key="index"
            :class="{ active: selectedOption === time.hour }"
            let="time"
            class="home__mid__cart"
            @click="showModalZapiz"
          >
            <input
              v-model="selectedOption"
              hidden
              :value="time.hour"
              :key="index"
              name="time"
              id="time"
              type="radio"
            />
            <span class="home__mid__cart-big">{{ time.hour }}</span>
            <span class="home__mid__cart-small">{{ time.minute }}</span>
          </label>
        </div>
        <SelectZapiz
          ref="modalZapiz"
          @create-appointment="createAppointment"
        ></SelectZapiz>
      </div>
    </div>
    <div class="home__bottom">
      <div class="container">
        <div class="home__bottom__cart aksii">
          <svg width="32" height="32">
            <use xlink:href="../../assets/img/sprite.svg#akcss"></use>
          </svg>
          <p>Скидки и акции</p>
          <span>Список спец предложений клиник</span>
        </div>
        <div class="home__bottom__cart">
          <svg width="32" height="32">
            <use xlink:href="../../assets/img/sprite.svg#zub"></use>
          </svg>
          <p>Клиники</p>
          <span>Список и рейтинг</span>
        </div>
        <div class="home__bottom__cart">
          <svg width="32" height="32">
            <use xlink:href="../../assets/img/sprite.svg#mozg"></use>
          </svg>
          <p>Специалисты</p>
          <span>Список и рейтинг</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SelectData from "./v-select-data.vue";
import SelectUsluga from "./v-select-usluga.vue";
import SelectZapiz from "./v-select-zapiz.vue";
import axios from "axios";
export default {
  name: "v-home",
  components: {
    SelectData,
    SelectUsluga,
    SelectZapiz,
  },
  data() {
    return {
      selectedOption: null,
      times: [
        {
          hour: "09",
          minute: "00",
        },
        {
          hour: "10",
          minute: "00",
        },
        {
          hour: "11",
          minute: "00",
        },
        {
          hour: "12",
          minute: "00",
        },
        {
          hour: "13",
          minute: "00",
        },
        {
          hour: "14",
          minute: "00",
        },
        {
          hour: "15",
          minute: "00",
        },
        {
          hour: "16",
          minute: "00",
        },

        {
          hour: "17",
          minute: "00",
        },
        {
          hour: "18",
          minute: "00",
        },
        {
          hour: "19",
          minute: "00",
        },
        {
          hour: "20",
          minute: "00",
        },
        {
          hour: "21",
          minute: "00",
        },
        {
          hour: "22",
          minute: "00",
        },
        {
          hour: "23",
          minute: "00",
        },
      ],
      uslugas: [],
      selectedDate: {
        day: 1,
        month: 11,
        year: 2023,
      },
      selectedUsluga: null,
    };
  },
  methods: {
    showModalDate: function () {
      this.$refs.modalDate.show = true;
    },
    showModalUsluga: function () {
      this.$refs.modalUsluga.show = true;
    },
    showModalZapiz: function () {
      this.$refs.modalZapiz.show = true;
    },
    loadServices() {
      axios
        .get("/specialist-list/")
        .then((response) => {
          console.log(response.data);
          this.uslugas = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleSelectedUsluga(selectedUslugaId) {
      this.selectedUslugaId = selectedUslugaId;
    },
    updateSelectedDate(selectedDate) {
      //Обновление только дня
      this.selectedDate.day = selectedDate.day;
    },
    createAppointment(selectedClinicId) {
      const appointmentData = {
        title: "test",
        service: this.selectedUslugaId,
        patient: this.$store.state.user_id,
        date:
          this.selectedDate.day +
          "." +
          this.selectedDate.month +
          "." +
          this.selectedDate.year,
        time: this.selectedOption+':00',
        status: "good",
        clinic: selectedClinicId,
      };
      axios
        .post("/appointment-add/", appointmentData)
        .then((response) => {
          console.log("Успеш", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.loadServices();
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

.aksii {
  background: linear-gradient(90deg, #5071e6 0%, #8b55e9 98.14%);
}

.home__bottom__cart.aksii,
.home__bottom__cart.aksii span {
  color: white;
}
</style>
