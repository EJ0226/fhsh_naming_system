<script setup>
import SmilePng from "../assets/Smile.png";
</script>

<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <div class="relative bg-[#D9D9D9] w-[300px] h-[375px] rounded-[30px]">
      <div class="w-[200px] h-[200px] mx-auto">
        <img :src="SmilePng" alt="SmilePng" />
      </div>
      <div>
        <p class="text-center font-bold text-[20px] mt-[20px]">
          您的商品已成功預購
        </p>
        //跳出通知
      </div>
      <div class="mt-[20px]">
        <p class="text-center">請匯款到此帳號()</p>
      </div>
      <div class="flex justify-center">
        <button
          class="w-[80px] h-[40px] rounded-[10px] absolute bottom-[20px] bg-[#ffffff]"
          @click="goToShop"
        >
          確認
        </button>
      </div>
    </div>
    <div></div>
  </div>
</template>

<script>
export default {
  methods: {
    goToShop() {
      this.$router.push("/shopUser");
    },
  },
}; //點完確定回到商品總頁面
</script>
