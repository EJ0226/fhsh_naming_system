<script setup>
import Login from "./page/Login.vue";
import DY from "./page/DeviceY.vue";
import Fail from "./page/FailPage.vue";
import CameraPage from "./page/CameraPage.vue";
import Confirm from "./page/Confirm.vue";
// import Camera from "./page/Camera.vue";
</script>

<template>
  <div class="h-mobile-screen w-screen overflow-x-hidden bg-[#FFFAF0]">
    <!-- 登入按鈕 -->
    <Login />

    <!-- 自拍 -->
    <CameraPage />

    <!-- 拍照畫面 -->
    <!-- <Camera /> -->

    <!-- 確認照片是否可以 -->
    <Confirm />

    <!-- 點名成功、有借設備 -->
    <DY />

    <!-- 點名失敗 -->
    <Fail />
  </div>
</template>
