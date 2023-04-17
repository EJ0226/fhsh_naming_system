<script>
export default {
  data() {
    return {
      showPassword: false,
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
      let passwordInput = this.$el.querySelector('input[type="password"]');
      if (this.showPassword) {
        passwordInput.setAttribute("type", "text");
      } else {
        passwordInput.setAttribute("type", "password");
      }
    },
    register() {},

    gotoLoginUser() {
      this.$router.push("/loginuser");
    },
  },
};
</script>
<template>
  <div class="overflow-x-hidden">
    <div class="relative w-screen flex flex-col items-center">
      <h1 class="font-black text-[4vw] text-center mt-[5vw] text-[#F59660]">
        帳號註冊
      </h1>
      <form>
        <div class="mt-[4vw] flex flex-col items-center">
          <label for="email" class="flex">
            <input
              type="text"
              placeholder="輸入您的email"
              class="w-[22vw] h-[4vw] text-[1.5vw] border-[0.25vw] border-[#F59660] rounded-md text-center mb-[2vw]"
              id="email"
            />

            <img
              src="../assets/CherryBlossoms.png"
              class="w-[3vw] h-[3vw] absolute ml-[18.6vw] mt-[0.6vw]"
            />
          </label>

          <div>
            <label for="password">
              <input
                type="password"
                placeholder="輸入您的密碼"
                class="w-[22vw] h-[4vw] text-[1.5vw] border-[0.25vw] border-[#F59660] rounded-md text-center mb-[2vw] focus:outline-none"
                id="“password”"
              />
              <button
                class="absolute ml-[-3.3vw] mt-[0.5vw]"
                @click="togglePassword"
              >
                <img
                  src="../assets/CherryBlossomSeeds.png"
                  alt="password visibility toggle"
                  class="w-[2vw] h-[3vw]"
                  :class="{ hidden: showPassword }"
                />
                <img
                  src="../assets/CherryBlossoms.png"
                  alt="password visibility toggle"
                  class="w-[3vw] h-[3vw]"
                  :class="{ hidden: !showPassword }"
                />
              </button>
            </label>
          </div>

          <label for="confirm-password">
            <input
              type="confirm-password"
              placeholder="確認密碼"
              class="w-[22vw] h-[4vw] text-[1.5vw] border-[0.25vw] border-[#F59660] rounded-md text-center mb-[2vw]"
              id="confirm-password"
            />
            <button
              class="absolute ml-[-3.3vw] mt-[0.5vw]"
              @click="togglePassword1"
            >
              <img
                src="../assets/CherryBlossomSeeds.png"
                alt="password visibility toggle"
                class="w-[2vw] h-[3vw]"
                :class="{ hidden: showPassword }"
              />
              <img
                src="../assets/CherryBlossoms.png"
                alt="password visibility toggle"
                class="w-[3vw] h-[3vw]"
                :class="{ hidden: !showPassword }"
              />
            </button>
          </label>
        </div>

        <div class="flex justify-center items-center mt-[2vw]">
          <button
            @click="gotoLoginUser"
            class="text-[1.5vw] w-[9vw] h-[3.5vw] border-[0.15vw] border-[#F59660] rounded-[1.2vw] text-[#F59660] flex justify-center items-center px-[1vw]"
          >
            已有帳號
          </button>
          <button
            @click="register"
            class="ml-[25px] text-[1.8vw] w-[9vw] h-[3.5vw] bg-[#F59660] rounded-[1.2vw] flex justify-center items-center text-white"
          >
            註冊
          </button>
        </div>
      </form>
      <div
        class="w-full h-[4vw] bg-[#F59660] mt-[8vw] text-white flex justify-center items-center text-[1.1vw]"
      >
        校址：112056臺北市北投區復興四路70號 <br />
        電話：02-28914131 傳真：02-28952156
      </div>
    </div>
  </div>
</template>
