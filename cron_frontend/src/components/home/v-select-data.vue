    <template>
    <div v-if="show" class="modal-shadow" @click.self="closeModal">
        <div class="modal">
        <div class="modal-close" @click="closeModal">
            <svg width="30" height="30">
            <use xlink:href="../../assets/img/sprite.svg#close"></use>
            </svg>
        </div>
        <div class="modal__nedelya">
            <span>ПН</span>
            <span>ВТ</span>
            <span>СР</span>
            <span>ЧТ</span>
            <span>ПТ</span>
            <span>СБ</span>
            <span>ВС</span>
        </div>
        <div class="modal__date">
            <label
            v-for="(date, index) in dates"
            :key="index"
            :class="{ active: selectedDate === date }"
            let="date"
            class="modal__date__cart"
            @click="selectDate(date)"
            >
            <input
                v-model="selectedDate"
                hidden
                :value="date"
                :key="index"
                name="date"
                id="date"
                type="radio"
            />
            <span class="home__mid__cart-big">{{ date.day }}</span>
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
    name: "SelectData",
    data: function () {
        return {
        show: false,
        selectedDate: null,
        dates: [
            {
            day: "01",
            },
            {
            day: "02",
            },
            {
            day: "03",
            },
            {
            day: "04",
            },
            {
            day: "05",
            },
            {
            day: "06",
            },
            {
            day: "07",
            },
            {
            day: "08",
            },
            {
            day: "09",
            },
            {
            day: "10",
            },
            {
            day: "11",
            },
            {
            day: "12",
            },
            {
            day: "13",
            },
            {
            day: "14",
            },
            {
            day: "15",
            },
            {
            day: "16",
            },

            {
            day: "17",
            },
            {
            day: "18",
            },
            {
            day: "19",
            },
            {
            day: "20",
            },
            {
            day: "21",
            },
            {
            day: "22",
            },
            {
            day: "23",
            },
            {
            day: "24",
            },
            {
            day: "25",
            },
            {
            day: "26",
            },
            {
            day: "27",
            },
            {
            day: "28",
            },
            {
            day: "29",
            },
            {
            day: "30",
            },
            {
            day: "31",
            },
        ],
        };
    },
    props: {
        parentDates: Array,
    },
    methods: {
        closeModal: function () {
        this.show = false;
        },
        selectDate(date) {
        if (!this.selectedDate) {
            this.selectedDate = {}; // Инициализация, если selectedDate не определен
        }
        this.selectedDate.day = date.day; // Обновление только дня
        this.$emit("selected-date", this.selectedDate);
        },
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

    .modal {
    background: var(--white);
    border-radius: 10px 10px 0 0;
    padding: 24px 20px;
    width: 100%;
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translate(-50%, 0%);
    padding-bottom: 88px;
    }

    .modal__nedelya {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    gap: 16px;
    }

    .modal__nedelya span {
    width: 32px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    }

    .modal-close {
    position: absolute;
    right: 0;
    top: -40px;
    }

    .modal__date {
    margin-top: 24px;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    gap: 16px;
    }

    .modal__date__cart {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: var(--grey);
    }

    .modal__date__cart.active {
    border-radius: 29px;
    background: var(--orange);
    color: var(--white);
    }
    </style>
