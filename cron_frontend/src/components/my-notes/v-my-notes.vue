<template>
    <div class="v-my-notes">
        <div class="my-notes-top">
            <div class="container">
                <div class="my-notes__title-item">
                    <h1 class="my-notes-title">
                        Мои<br>записи
                    </h1>
                    <div class="push">
                        <svg width="40" height="40">
                            <use xlink:href="../../assets/img/sprite.svg#push"></use>
                        </svg>
                    </div>
                </div>
                <p class="my-notes-top-p">
                    Ваши актуальные записи
                </p>
            </div>
        </div>
        <vNotes></vNotes>
    </div>
</template>

<script>
    import vNotes from './v-notes.vue'

    export default {
        name: 'v-my-notes',
        components: {
            vNotes
        },
        data() {
            return {
            }
        }
    }
</script>
<style>
    .v-my-notes{
        display: block;
        margin-bottom: 88px;
    }

    .my-notes-top{
        padding: 30px 0 20px;
        background-color: var(--white);
        border-radius: 0 0 20px 20px;
        margin-bottom: 20px;
        display: block;
    }

    .my-notes__title-item{
        display: flex;
        justify-content: space-between;
    }

    .my-notes-title{
        font-size: 40px;
        font-weight: 500;
        letter-spacing: -1.6px;
        margin-bottom: 4px;
    }

    .my-notes-top-p{
        line-height: 150%; 
        letter-spacing: -0.176px;
        color: var(--grey);
    }
</style>