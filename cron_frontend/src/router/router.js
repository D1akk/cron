import { createRouter, createWebHashHistory } from "vue-router";

import vHome from "../components/home/v-home";
import vMyNotes from "../components/my-notes/v-my-notes";
import vDoctors from "../components/doctors/v-doctors";
import vProfile from "../components/profile/v-profile";
import vLogin from "../components/login/v-login";

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: vHome,
    },
    {
      path: "/my-notes",
      name: "my-notes",
      component: vMyNotes,
    },
    {
      path: "/doctors",
      name: "doctors",
      component: vDoctors,
    },
    {
      path: "/profile",
      name: "profile",
      component: vProfile,
    },
    {
      path: "/login",
      name: "login",
      component: vLogin,
    },
  ],
});
