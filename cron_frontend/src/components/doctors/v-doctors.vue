<template>
    <div class="v-doctors">
        <div class="doctors-top">
            <div class="container">
                <div class="doctors__title-item">
                    <h1 class="doctors-title">
                        Врачи
                    </h1>
                    <div class="push">
                        <svg width="40" height="40">
                            <use xlink:href="../../assets/img/sprite.svg#push"></use>
                        </svg>
                    </div>
                </div>
                <p class="doctors-top-p">
                    Рейтинг врачей
                </p>
            </div>
        </div>
        <vDoctorCard></vDoctorCard>
    </div>
</template>

<script>
    import vDoctorCard from './v-doctor-card.vue'

    export default {
        name: 'v-doctors',
        components: {
            vDoctorCard
        },
        data() {
            return {
                
            };
        }
    }
</script>
<style>
    .v-doctors{
        display: block;
        margin-bottom: 88px;
    }

    .doctors-top{
        padding: 30px 0 20px;
        background-color: var(--white);
        border-radius: 0 0 20px 20px;
        display: block;
        margin-bottom: 20px;
    }

    .doctors__title-item{
        display: flex;
        justify-content: space-between;
        margin-bottom: 4px;
    }

    .doctors-title{
        font-size: 40px;
        font-weight: 500;
        letter-spacing: -1.6px;
    }

    .doctors-top-p{
        line-height: 150%;
        letter-spacing: -0.176px;
        color: var(--grey);
    }
    
</style>