// import { createApp } from "vue";
import "./style.css";
// import App from "./App.vue";

createApp(App).mount("#app");

import { createApp } from "vue";
import App from "./App.vue";

const app = createApp(App);

// app.use(router);

// app.mount("#app");

import { createRouter, createWebHistory } from "vue-router";
import login from "./page/Login.vue";
import dy from "./page/DeviceY.vue";
import fail from "./page/FailPage.vue";
import camerapage from "./page/CameraPage.vue";
import confirm from "./page/Confirm.vue";
// import camera from "./page/Camera.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: login,
    },
    {
      path: "/dy",
      component: dy,
    },

    {
      path: "/fail",
      component: fail,
    },
    {
      path: "/camerapage",
      component: camerapage,
    },
    {
      path: "/confirm",
      component: confirm,
    },
    // {
    //   path: "/camera",
    //   component: camera,
    // },
  ],
});
