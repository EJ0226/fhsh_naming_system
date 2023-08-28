import { createRouter, createWebHistory } from "vue-router";
import login from "./page/Login.vue";
import camerapage from "./page/CameraPage.vue";
// // import camera from "./page/Camera.vue";
// import confirm from "./page/Confirm.vue";
import dy from "./page/DeviceY.vue";
import fail from "./page/FailPage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: login,
    },
    {
      path: "/camerapage",
      component: camerapage,
    },
    // {
    //   path: "/camera",
    //   component: camera,
    // },
    // {
    //   path: "/confirm",
    //   component: confirm,
    // },
    {
      path: "/dy",
      component: dy,
    },
    {
      path: "/fail",
      component: fail,
    },
  ],
});

export default router;
