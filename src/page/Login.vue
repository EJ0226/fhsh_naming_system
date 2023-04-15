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

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      errorMsg: "",
    };
  },
  methods: {
    login() {
      if (!this.username || !this.password) {
        this.errorMsg = "帳號名稱或密碼不能為空";
        return;
      }
    },
  },
};
</script>
