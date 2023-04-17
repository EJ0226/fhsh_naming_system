<template>
  <div class="w-screen h-screen flex flex-col items-center">
    <h1 class="font-black text-[40px] text-center mt-[60px]">帳號登入</h1>
    <form @submit.prevent="login">
      <div class="mt-[60px]">
        <label for="email">
          <input
            id="username"
            v-model.trim="username"
            required
            minlength="3"
            maxlength="20"
            type="text"
            placeholder="輸入您的帳號名稱"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
          />
        </label>
        <br />
        <label for="password">
          <input
            id="password"
            v-model.trim="password"
            required
            minlength="6"
            maxlength="16"
            type="password"
            placeholder="輸入您的密碼"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
          />
        </label>
      </div>
      <button @click="gotoregister">已有帳號</button>
      <div class="flex justify-center items-center mt-[30px]">
        <button
          type="submit"
          class="w-[77px] h-[44px] bg-[#D9D9D9] rounded-[15px] text-[24px] flex justify-center items-center"
        >
          登入
        </button>
      </div>
    </form>
    <div v-if="errorMsg">{{ errorMsg }}</div>
  </div>
</template>

<script setup>
import axios from "axios";
import { reactive } from "vue";

const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

const errorMsg = ref("");
const formdata = reactive({
  username: "",
  password: "",
});
//輸入帳號密碼，跟後端確認用戶資料

login = async () => {
  const data = reactive({
    username: formdata.username,
    password: formdata.password,
  });
  gotoregister = () => {
    router.push("/");
  };

  if (!username.value || password.value) {
    errorMsg.value = "帳號名稱或密碼不能為空";
    return;
  }
  await request
    .post("/signin", data)
    .then((response) => {
      response.data.access_token = localStorage.getItem(
        "access_token",
        response.data.access_token
      );
      router.push("/"); //登入之後要去哪? front page?
    })
    .catch((error) => {
      if (error.response.status === 401) {
        errorMsg.value = "帳號不存在";
      }
    });
}; //如果帳號密碼錯誤顯現"帳號名稱或密碼不能為空"//輸入成功的話上方標示帳號/密碼
</script>
