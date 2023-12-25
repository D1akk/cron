<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">
        <svg width="30" height="30">
          <use xlink:href="../../assets/img/sprite.svg#close"></use>
        </svg>
      </div>
      <div class="modal__usluga">
        <label
          v-for="(parentUsluga, index) in parentUslugas"
          :key="index"
          :class="{ active: selectedUsluga === parentUsluga }"
          let="usluga"
          class="modal__usluga__cart"
        >
          <input
            v-model="selectedUsluga"
            hidden
            :value="parentUsluga"
            :key="index"
            name="usluga"
            id="usluga"
            type="radio"
            @change="emitSelectedUsluga(parentUsluga.id)"
          />
          <span class="home__mid__cart-big">{{ parentUsluga.type }}</span>
        </label>
      </div>
      <!-- <slot name="footer">
                <div class="modal-footer">
                    <button class="modal-footer__button" @click="closeModal">
                        Ок
                    </button>
                </div>
            </slot> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "SelectUsluga",
  data: function () {
    return {
      show: false,
      selectedUsluga: null,
    };
  },
  props: {
    parentUslugas: Array,
  },
  methods: {
    closeModal: function () {
      this.show = false;
    },
    emitSelectedUsluga: function (selectedUslugaId) {
      this.$emit("selected-usluga", selectedUslugaId); // Эмитирование события с выбранным ID услуги
      // this.show = false; // Закрываем модальное окно после выбора
    },
  },
};
</script>

<style>
.modal__usluga {
  display: grid;
  gap: 20px;
}

.modal__usluga__cart {
  display: block;
}

.modal__usluga__cart.active {
  color: var(--orange);
}
</style>
