<template>
  <div class="h-screen bg-[#FFFAF0]">
    <div class="flex justify-between">
      <div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      </div>
      <div
        class="text-right text-[#97AEB9] font-semibold text-md leading-9 pr-7"
      >
        <div class="p-1"></div>
        復興高中<br />自主學習點名系統
      </div>
    </div>
    <div class="">
      <video id="video" class="w-32 h-24 autoplay"></video>
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
import { onMounted, ref } from "vue";

const video = ref(null);
const videoObj = { video: true, audio: true };

const errBack = (error) => {
  console.log("Video capture error: ", error.code);
};

onMounted(() => {
  if (navigator.mediaDevices.getUserMedia) {
    // 使用标准API
    navigator.mediaDevices
      .getUserMedia(videoObj)
      .then((stream) => {
        video.value.srcObject = stream;
        video.value.play();
      })
      .catch(errBack);
  } else if (navigator.webkitGetUserMedia) {
    // WebKit-prefixed
    navigator.webkitGetUserMedia(
      videoObj,
      (stream) => {
        video.value.src = window.webkitURL.createObjectURL(stream);
        video.value.play();
      },
      errBack
    );
  } else if (navigator.mozGetUserMedia) {
    // Firefox-prefixed
    navigator.mozGetUserMedia(
      videoObj,
      (stream) => {
        video.value.src = window.URL.createObjectURL(stream);
        video.value.play();
      },
      errBack
    );
  } else if (navigator.msGetUserMedia) {
    navigator.msGetUserMedia(
      videoObj,
      (stream) => {
        video.value.src = window.URL.createObjectURL(stream);
        video.value.play();
      },
      errBack
    );
  }
});
</script>
