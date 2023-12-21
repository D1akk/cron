<template>
  <footer class="v-footer">
    <div class="footer">
      <div class="container">
        <nav class="footer-nav">
          <ul class="footer-ul">
            <li class="footer-li">
              <router-link :to="{ name: 'home' }">
                <svg width="24" height="24">
                  <use xlink:href="../../assets/img/sprite.svg#home"></use>
                </svg>
                <span>Главная</span>
              </router-link>
            </li>
            <li class="footer-li">
              <router-link :to="{ name: 'my-notes' }">
                <svg width="24" height="24">
                  <use xlink:href="../../assets/img/sprite.svg#zapiz"></use>
                </svg>
                <span>Мои записи</span>
              </router-link>
            </li>
            <li class="footer-li">
              <router-link :to="{ name: 'doctors' }">
                <svg width="24" height="24">
                  <use xlink:href="../../assets/img/sprite.svg#vrach"></use>
                </svg>
                <span>Врачи</span>
              </router-link>
            </li>
            <li class="footer-li">
              <router-link :to="{ name: 'profile' }">
                <svg width="24" height="24">
                  <use xlink:href="../../assets/img/sprite.svg#profile"></use>
                </svg>
                <span>Профиль</span>
              </router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: "v-footer",
};
</script>
<style>
.footer {
  background-color: white;
  position: fixed;
  bottom: 0;
  z-index: 1000;
  width: 100%;
  padding: 14px 0;
  border-radius: 20px 20px 0px 0px;
  box-shadow: 0px -1px 4px 0px rgba(0, 0, 0, 0.25);
}

.footer-ul {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  align-items: center;
}

.footer-li {
  list-style-type: none;
  font-size: 12px;
}

.footer-li a {
  font-size: 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
