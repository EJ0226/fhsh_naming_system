<template>
  <div class="bg-[#FAF7EF] h-screen">
    <div class="flex justify-between">
      <div>
        <div class="p-4"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      </div>
      <div
        class="text-right text-[#97AEB9] font-semibold text-md leading-9 pr-7"
      >
        <div class="p-3"></div>
        復興高中<br />自主學習點名系統
      </div>
    </div>

    <div class="pt-6"></div>

    <div class="flex justify-center items-center flex-col">
      <div class="">
        <video ref="video" class="w-56 h-48 autoplay"></video>
      </div>
      <div class="flex justify-center items-center">
        <button
          class="rounded-md text-center bg-white py-3 px-6 border border-[#97aeb9]"
          id="openCameraButton"
          @click="isCameraOpen ? takePhoto() : openCamera()"
        >
          <span class="text-[#97aeb9] font-semibold text-xl">
            {{ isCapturing ? "拍照中..." : isCameraOpen ? "拍照" : "開啟相機" }}
          </span>
        </button>
      </div>
      <img v-if="capturedImage" :src="capturedImage" class="pt-5 w-56 h-48" />

      <div class="pt-3"></div>
      <button
        class="bg-[#698694] py-3 px-6 rounded-md text-center shadow-md"
        id="openCameraButton"
        v-if="capturedImage"
      >
        <span class="text-white font-semibold text-xl">確定</span>
      </button>
    </div>

    <div class="absolute flex flex-col items-end right-0">
      <div class="p-6"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      <div class="p-2"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
      <div class="p-2"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const video = ref(null);
const capturedImage = ref(null);
const isCameraOpen = ref(false);
const isCapturing = ref(false);

const videoObj = { video: true, audio: true };

const errBack = (error) => {
  console.log("影像擷取錯誤: ", error.code);
};

const openCamera = () => {
  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices
      .getUserMedia(videoObj)
      .then((stream) => {
        video.value.srcObject = stream;
        video.value.play();
        isCameraOpen.value = true;
      })
      .catch(errBack);
  }
};

const takePhoto = () => {
  if (isCameraOpen.value) {
    isCapturing.value = true;

    const videoElement = video.value;
    const canvas = document.createElement("canvas");
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    const ctx = canvas.getContext("2d");

    ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    const imageDataUrl = canvas.toDataURL("image/jpeg");
    capturedImage.value = imageDataUrl;

    isCapturing.value = false;
  }
};

// const navigateToPage = () => {
//   if (capturedImage.value) {
//     // 图片上传成功后，根据条件决定跳转到不同的页面
//     if (条件) {
//       // 根据条件跳转到 /dy 页面
//       router.push({ name: "dy" });
//     } else {
//       // 否则跳转到 /fail 页面
//       router.push({ name: "fail" });
//     }
//   }
// };

// const navigateToPage = () => {
//   router.push("/dy");
// };
</script>
<!-- @click="navigateToPage" -->
