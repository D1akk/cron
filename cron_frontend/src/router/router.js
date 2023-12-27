import { createRouter, createWebHashHistory } from "vue-router";

import vHome from "../components/home/v-home";
import vMyNotes from "../components/my-notes/v-my-notes";
import vDoctors from "../components/doctors/v-doctors";
import vProfile from "../components/profile/v-profile";
import vLogin from "../components/login/v-login";
import vSignup from "../components/signup/v-signup";

const routes = [
  {
    path: "/",
    name: "home",
    component: vHome,
    meta: { requiresAuth: true },
  },
  {
    path: "/my-notes",
    name: "my-notes",
    component: vMyNotes,
    meta: { requiresAuth: true },
  },
  {
    path: "/doctors",
    name: "doctors",
    component: vDoctors,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "profile",
    component: vProfile,
    meta: { requiresAuth: true },
  },
  {
    path: "/login",
    name: "login",
    component: vLogin,
    meta: { requiresAuth: false },
  },
  {
    path: "/signup",
    name: "signup",
    component: vSignup,
    meta: { requiresAuth: false },
  },
];

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
});

const protectedRoutes = ["my-notes", "doctors", "profile", "home"];

// router.beforeEach((to, from, next) => {
//   const isProtected = protectedRoutes.includes(to.name);
//   if (isProtected && !localStorage.getItem("token")) {
//     next({
//       path: "/",
//       query: { redirect: to.fullPath },
//     });
//   } else {
//     if (
//       !isProtected &&
//       localStorage.getItem("token") &&
//       (to.name == "home" || to.name == "signup")
//     ) {
//       next({
//         path: "",
//       });
//     } else {
//       next();
//     }
//   }
// });

router.beforeEach((to, from, next) => {
  const isProtected = protectedRoutes.includes(to.name);
  const isAuthenticated = localStorage.getItem("token");

  if (isProtected && !isAuthenticated) {
    next({ name: "login", query: { redirect: to.fullPath } });
  } else if (!isProtected && isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
