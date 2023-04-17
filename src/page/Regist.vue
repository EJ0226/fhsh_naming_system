<template>
  <div class="w-screen h-screen flex flex-col items-center">
    <h1 class="font-black text-[40px] text-center mt-[60px]">帳號註冊</h1>

    <div class="mt-[60px]">
      <form v-on:submit.prevent="regist">
        <div>
          <label for="email">帳號名稱:</label>
          <br />
          <input
            minlength="3"
            maxlength="20"
            type="text"
            placeholder="請輸入3-20個字符"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="email"
          />
        </div>
        <div>
          <label for="password">輸入密碼:</label>
          <br />
          <input
            minlength="6"
            maxlength="16"
            type="password"
            placeholder="請輸入6-16個字符"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="“password”"
          />
        </div>
        <div>
          <label for="confirm-password">確認密碼:</label>
          <br />
          <input
            minlength="6"
            maxlength="16"
            type="password"
            placeholder="請再次確認密碼"
            class="w-[240px] h-[40px] bg-[#D9D9D9] text-center mb-[30px]"
            id="confirm-password"
          />
        </div>

        <div class="flex justify-center items-center mt-[30px]">
          <button class="text-[24px] underline" @click="goToLogoin">
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

<script>
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    regist() {
      // 在這裡呼叫後端API進行註冊處理
      // 如果註冊成功，導航到登入頁面
      this.$router.push("/login");
    },

    goToLogoin() {
      this.$router.push("/login");
    },
  },
};
</script>
