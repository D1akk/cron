<template>
    <div class="v-doctor-card">
        <div class="doctor-card" v-for="(doctor, index) in doctors" :key="index">
            <div class="doctor-card__top">
                <img :src=" require('../../assets/img/' + doctor.photo)" alt="">
                <div>
                    <div>
                        <span class="doctor-card__top-name">{{ doctor.name }}</span>
                    </div>
                    <div style="display: flex; align-items:center; justify-content:space-between ">
                        <div>
                            <span class="doctor-card__top-reyting">{{ doctor.reyting }}</span>
                            <span class="doctor-card__top-reyting-text">{{ doctor.reytingText }}</span>
                            <span class="doctor-card__top-osenki">{{ doctor.osenki }}</span>
                        </div>
                        <span class="doctor-card__top-stazh">{{ doctor.stazh }}</span>
                    </div>
                </div>
            </div>
            <div class="doctor-card__mid">
                <div class="doctor-card__mid__flex">
                    <div>
                        <span class="doctor-card__mid-otzivFio">{{ doctor.otzivFio }}</span>
                        <br>
                        <span class="doctor-card__mid-reyting">{{ doctor.reyting }}</span>
                    </div>
                    <span class="doctor-card__mid-otzivDay">{{ doctor.otzivDay }}</span>
                </div>
                <p class="doctor-card__mid-p">
                    Этому врачу нужно перестать много думать, у меня болел зуб мудрости, а он мне предложил создать агрегатор по соединению CRM с AI (искусственным интеллектом), слишком все усложнил, а так специалист хороший
                </p>
                <div class="doctor-card__mid-a">
                    <a href="#">Посмотреть отзывы</a>
                </div>
            </div>
            <div class="doctor-card__bottom">
                <a @click="showModalDate">Записаться на прием </a>
            </div>
            
        </div>
    </div>
</template>

<script>
    
    export default {
        name: 'v-doctor-card',
        components: {
        
        },
        data() {
            return {
                doctors: [
                    {
                        name: 'Аржаков Сергей',
                        photo: 'sergey.png',
                        reyting: '★★★★☆',
                        reytingText: '4.0',
                        osenki: '16 оценок',
                        stazh: 'Стаж 6 лет',
                        otzivFio: 'Иванов Артем',
                        otzivDay: '3 дня назад',
                        otzivComment: 'Этому врачу нужно перестать много думать, у меня болел зуб мудрости, а он мне предложил создать агрегатор по соединению CRM с AI (искусственным интеллектом), слишком все усложнил, а так специалист хороший  ',
                    },
                    {
                        name: 'Дьячковский Александр',
                        photo: 'lesha.png',
                        reyting: '★★★★☆',
                        reytingText: '5.0',
                        stazh: 'Стаж 24 лет',
                        osenki: '124 оценок',
                        otzivFio: 'Ефремов Николай',
                        otzivDay: '6 дней назад',
                        otzivComment: 'Подарил видеокарту, я пришел лечить зуб ушел довольный, как слон. Правда содрали за услугу в два раза больше, чем рассчитывал, а так газон на территории стоматологии хороший сразу видно стоит целый лям',
                    },
                    {
                        name: 'Щенникова Дарья',
                        photo: 'dasha.png',
                        reyting: '★★★★☆',
                        reytingText: '4.0',
                        stazh: 'Стаж 4 лет',
                        osenki: '13 оценок',
                        otzivFio: 'Полина Третьякова',
                        otzivDay: '1 день назад',
                        otzivComment: 'Врач отличный, к дополнению к лечению научила играть в карты и разговаривать на зыряновском жаргоне. Правда я проиграла в Пикало и пришлось заплатить 500 рублей наликом',
                    },
                ],
                selectedOption: null,
            };
        }
    }
</script>
<style>
    .v-doctor-card{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .doctor-card{
        padding: 20px 16px;
        background-color: var(--white);
        border-radius: 20px;
    }

    .doctor-card__top{
        padding-bottom: 20px;
        display: grid;
        grid-template-columns: 56px 1fr;
        gap: 10px;
        align-items: center;
        border-bottom: 1px solid var(--light-grey);
    }

    .doctor-card__top img{
        width: 56px;
        height: 56px;
        border-radius: 8px;
    }

    .doctor-card__top-name{
        font-size: 20px;
        font-weight: 400;
        letter-spacing: -0.8px;
        margin-bottom: 10px;
        display: block;
    }

    .doctor-card__top-reyting{
        font-size: 18px;
        line-height: 16px;
        color: #FFAD32;
        margin-right: 4px;
    }

    .doctor-card__top-reyting-text{
        margin-right: 10px;
    }

    .doctor-card__top-osenki{
        color: var(--grey);
        font-size: 12px;
        letter-spacing: -0.48px;
    }

    .doctor-card__top-stazh{
        color: var(--grey);
        font-size: 12px;
        letter-spacing: -0.48px;
    }

    .doctor-card__mid{
        padding: 20px 0;
        border-bottom: 1px solid var(--light-grey);
    }

    .doctor-card__mid__flex{
        display: flex;
        justify-content: space-between;
        margin-bottom: 8px;
    }

    .doctor-card__mid-otzivFio{
        font-size: 12px;
        letter-spacing: -0.48px;
    }

    .doctor-card__mid-reyting{
        color: #FFAD32;
        font-size: 12px;
    }

    .doctor-card__mid-otzivDay{
        font-size: 12px;
        letter-spacing: -0.48px;
        color: var(--grey);
    }

    .doctor-card__mid-p{
        font-size: 12px;
        letter-spacing: -0.48px;
        margin-bottom: 10px;
    }

    .doctor-card__mid-a{
        display: flex;
        justify-content: end;
    }

    .doctor-card__mid-a a{
        color: var(--orange);
        line-height: 150%; /* 21px */
        letter-spacing: -0.154px;
    }

    .doctor-card__bottom{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .doctor-card__bottom a{
        color: var(--blue);
        line-height: 150%; /* 21px */
        letter-spacing: -0.154px;
    }
</style>