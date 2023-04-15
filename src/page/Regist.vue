<template>
  <div class="w-screen h-screen flex flex-col items-center">
    <h1 class="font-black text-[40px] text-center mt-[60px]">帳號註冊</h1>
    <div class="mt-[60px]">
  <form @:submit.prevent="regist">
    <div>
      <label for="username">使用者名稱:</label>
      <br />
      <input
        minlength="7"
        maxlength="20"
        type="text"
        placeholder="請輸入7-20個字符"
        class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
        id="username"
        name="username"
        v-model="formData.username"
      />
    </div>
    <div>
      <label for="email">email:</label>
      <br />
      <input
        minlength="3"
        maxlength="20"
        type="text"
        placeholder="請輸入3-20個字符"
        class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
        id="email"
        name="email"
        v-model="formData.email"
      />
    </div>
    <div>
      <label for="password">輸入密碼:</label>
      <br />
      <input
        minlength="7"
        maxlength="16"
        type="password"
        placeholder="請輸入7-16個字符"
        class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
        id="password"
        name="password"
        v-model="formData.password"
      />
    </div>
    <div>
      <label for="checkpassword">確認密碼:</label>
      <br />
      <input
        minlength="6"
        maxlength="16"
        type="password"
        placeholder="請再次確認密碼"
        class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
        id="check-password"
        name="checkpassword"
        v-model="formData.checkpassword"
      />
    </div>
    <div class="flex justify-center items-center mt-[30px]">
      <button class="text-[24px] underline" @click.prevent="goToLogin">
        已有帳號
      </button>
      <button
        type="submit"
        class="ml-[25px] w-[77px] h-[44px] bg-[#D9D9D9] rounded-[15px] text-[24px] flex justify-center items-center"
      >
        註冊
      </button>
    </div>
  </form>
</div>
</div>
</template>

<script setup>
import axios from "axios"
import { ref, reactive} from "vue"
import { useRouter } from "vue-router"

const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
})

    const message = ref("")
    const formData = reactive({
      username: "",
      checkpassword: "",
      email: "",
      password: "",
    });
    const router = useRouter()

    const regist = () => {
      const data = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        checkpassword: formData.checkpassword,
      }
      request.post("/register", data)
        .then(response => {
          message.value = response.data
          router.push("/login");
        })
        .catch(error => {
          message.value = error.response.data
        })
    const goToLogin = () => {
      router.push("/login");
    }
}
</script>

