<!-- <script setup>
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD8tawmKYehwLXxhX-l7YuFJDOMXfiTYw4",
  authDomain: "naming-system-396005.firebaseapp.com",
  projectId: "naming-system-396005",
  storageBucket: "naming-system-396005.appspot.com",
  messagingSenderId: "414969189132",
  appId: "1:414969189132:web:03f6858b64cf5a4995ef29",
  measurementId: "G-X0358YVEBG",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const auth = getAuth();

const loginWithGoogle = async () => {
  try {
    const provider = new GoogleAuthProvider();
    await signInWithPopup(auth, provider);

    console.log("Success!");
  } catch (error) {
    console.error("Fail!", error);
  }
};
</script> -->

<!-- <template>
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
    <a
      class="flex justify-center items-center"
      :href="authUrl"
      target="_blank"
      @click="loginWithGoogle"
    >
      <div class="py-56"></div>
      <button class="bg-[#698694] py-5 px-20 rounded-xl text-center shadow-md">
        <span class="text-white font-bold text-4xl">登入</span>
      </button>
    </a>

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

 -->

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

    <!-- 添加 Google 登录按钮 -->
    <div class="flex justify-center items-center">
      <div class="py-56"></div>
      <button
        class="bg-[#698694] py-5 px-20 rounded-xl text-center shadow-md"
        @click="loginWithGoogle"
      >
        <span class="text-white font-bold text-4xl">登入</span>
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
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyD8tawmKYehwLXxhX-l7YuFJDOMXfiTYw4",
  authDomain: "naming-system-396005.firebaseapp.com",
  projectId: "naming-system-396005",
  storageBucket: "naming-system-396005.appspot.com",
  messagingSenderId: "414969189132",
  appId: "1:414969189132:web:03f6858b64cf5a4995ef29",
  measurementId: "G-X0358YVEBG",
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// 获取 Firebase 身份验证实例
const auth = getAuth();

// 登录方法
const loginWithGoogle = async () => {
  try {
    const provider = new GoogleAuthProvider();
    await signInWithPopup(auth, provider);

    console.log("Success!");
  } catch (error) {
    console.error("Fail!", error);
  }
};
</script>
