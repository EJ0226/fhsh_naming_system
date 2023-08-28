<script setup>
import Login from "./page/Login.vue";
import DY from "./page/DeviceY.vue";
import Fail from "./page/FailPage.vue";
import CameraPage from "./page/CameraPage.vue";
// import Confirm from "./page/Confirm.vue";
// import Camera from "./page/Camera.vue";
</script>

<template>
  <div class="h-screen w-screen overflow-x-hidden bg-[#FFFAF0]">
    <nav>
      <div>
        <router-link to="/"></router-link>
        <router-link to="/camerapage"></router-link>
        <router-link to="/dy"></router-link>
        <router-link to="/fail"></router-link>

        <router-view />
      </div>
    </nav>

    <!-- 登入按鈕 -->
    <Login />

    <!-- 自拍 -->
    <CameraPage />

    <!-- 拍照畫面 -->
    <!-- <Camera /> -->

    <!-- 確認照片是否可以 -->
    <!-- <Confirm /> -->

    <!-- 點名成功、有借設備 -->
    <DY />

    <!-- 點名失敗 -->
    <Fail />
    <nav>
      <div>
        <router-link to="/"></router-link>
        <router-link to="/camerapage"></router-link>
        <router-link to="/dy"></router-link>
        <router-link to="/fail"></router-link>

        <router-view />
      </div>
    </nav>
  </div>
</template>
