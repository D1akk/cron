<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal-zapiz">
      <div class="modal-close" @click="closeModal">
        <svg width="30" height="30">
          <use xlink:href="../../assets/img/sprite.svg#close"></use>
        </svg>
      </div>
      <div v-for="(clinic, index) in clinics" :key="index" class="modal__zapiz">
        <span class="modal__zapiz-name">{{ clinic.title }}</span>
        <div class="modal__zapiz-flex">
          <!-- <div class="modal__zapiz-flex-item">
            <span class="modal__zapiz-reyting">{{ klinic.reyting }}</span>
            <span class="modal__zapiz-reytingNaz">{{ klinic.reytingNaz }}</span>
          </div> -->
          <!-- <span class="modal__zapiz-osenki">{{ klinic.osenki }}</span> -->
        </div>
        <div class="gwegwegwegwegfw">
          <span class="modal__zapiz-street">{{ clinic.location }}</span>
          <!-- <span class="modal__zapiz-radius">{{ klinic.radius }}</span> -->
        </div>
        <!-- <div class="afwegqf">
          <span>{{ klinic.type }}</span>
          <span>{{ klinic.price }}</span>
        </div> -->
        <span class="modal__zapiz-info"
          >Окончательная цена устанавливается после осмотра</span
        >
        <!-- <form> -->
        <!-- <input type="text" name="clinic" :value="clinic.title" /> -->

        <a
          @click="createAppointmentAndCloseModal(clinic.id)"
          class="modal__zapiz-a"
          href="#"
          >Записаться</a
        >
        <!-- </form> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SelectZapiz",
  data: function () {
    return {
      show: false,
      clinics: [
        // {
        //     name: 'Династия',
        //     reyting: '★★★★☆',
        //     reytingNaz: '4.0',
        //     osenki: '57 оценок',
        //     street: 'Короленко 17,  1 этаж',
        //     radius: 'Рядом',
        //     type: 'Протезирование ',
        //     price: 'от 6 000₽',
        //     info: 'Окончательная цена устанавливается после осмотра'
        // },
        // {
        //     name: 'Vita-Sens',
        //     reyting: '★★★★☆',
        //     reytingNaz: '4.0',
        //     osenki: '57 оценок',
        //     street: 'Короленко 17,  1 этаж',
        //     radius: 'Рядом',
        //     type: 'Протезирование ',
        //     price: 'от 6 000₽',
        //     info: 'Окончательная цена устанавливается после осмотра'
        // },
        // {
        //     name: 'Vita-Sens',
        //     reyting: '★★★★☆',
        //     reytingNaz: '4.0',
        //     osenki: '57 оценок',
        //     street: 'Короленко 17,  1 этаж',
        //     radius: 'Рядом',
        //     type: 'Протезирование ',
        //     price: 'от 6 000₽',
        //     info: 'Окончательная цена устанавливается после осмотра'
        // },
      ],
    };
  },
  methods: {
    closeModal: function () {
      this.show = false;
    },
    loadClinics() {
      axios
        .get("/clinic-list/")
        .then((response) => {
          this.clinics = response.data;
          //   console.log(this.doctors);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    createAppointmentAndCloseModal: function (selectedClinicId) {
      this.$emit("create-appointment", selectedClinicId);
      this.closeModal();
      alert("Запись успешно создана");
    },
  },
  mounted() {
    this.loadClinics();
  },
};
</script>

<style>
.modal-shadow {
  position: absolute;
  top: 0;
  left: 0;
  min-height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.39);
  z-index: 1000;
}

.modal-zapiz {
  background: var(--white);
  border-radius: 10px 10px 0 0;
  padding: 24px 20px;
  width: 100%;
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translate(-50%, 40%);
  padding-bottom: 88px;
}

.modal-close {
  position: absolute;
  right: 0;
  top: -40px;
}

.modal__zapiz-name {
  font-size: 20px;
  letter-spacing: -0.8px;
  margin-bottom: 10px;
}

.modal__zapiz-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  margin-top: 8px;
}

.modal__zapiz-flex-item {
  display: flex;
  align-items: center;
}

.modal__zapiz-reyting {
  color: #ffad32;
  font-size: 18px;
  line-height: 18px;
}

.modal__zapiz-osenki {
  color: var(--grey);
}
.gwegwegwegwegfw {
  display: flex;
  margin: 10px 0 20px;
  align-items: center;
  justify-content: space-between;
}

.modal__zapiz-street {
  display: block;
  font-size: 12px;
}

.modal__zapiz-radius {
  display: block;
  font-size: 12px;
  color: var(--blue);
}

.afwegqf {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.modal__zapiz-info {
  color: var(--grey);
  font-size: 12px;
}

.modal__zapiz-a {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--blue);
  color: white;
  padding: 12px;
  border-radius: 10px;
  margin: 8px 0 50px;
}
</style>
