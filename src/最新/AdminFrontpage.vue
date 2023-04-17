<script setup>
import searchSvg from "../assets/magnifying-glass-solid.svg";
import plusSvg from "../assets/plus-solid.svg";
</script>

<template>
  <div>
    <div class="w-full h-[6vw] bg-[#F28383] flex items-center">
      <button @click="goToEdit" class="ml-[1vw]">
        <img :src="searchSvg" alt="searchSvg" class="w-[40px] h-[40px]" />
      </button>
      <input
        class="w-[50vw] h-[4vw] border-[0.5vw] ml-[1.5vw] border-white rounded-[0.8vw] text-[2vw] text-center"
        placeholder="搜尋想查找的商品"
      />
      <button @click="goToEdit" class="ml-auto mr-[1vw]">
        <img :src="plusSvg" alt="plusSvg" class="w-[40px] h-[40px]" />
      </button>
    </div>
    <div class="flex justify-center items-center my-[8.5vw]">
      <div class="text-center text-[3vw] font-bold pr-[10vw]">Admin</div>
      <div class="border-l border-black h-[20vw] px-[10vw]"></div>
      <div class="flex justify-center items-center">
        <button
          @click="goToShop"
          class="w-[15vw] h-[15vw] border-black border-[0.2vw] font-bold text-[2vw] mr-[3vw]"
        >
          瀏覽商品
        </button>
        <button
          @click="goToOrder"
          class="w-[15vw] h-[15vw] border-black border-[0.2vw] font-bold text-[2vw] ml-[3vw]"
        >
          訂單查詢
        </button>
      </div>
    </div>
  </div>
  <div
    class="w-full h-[10vw] bg-[#F28383] text-white flex justify-center items-center text-[2.2vw]"
  >
    校址：112056臺北市北投區復興四路70號 <br />
    電話：02-28914131 傳真：02-28952156
  </div>
</template>

<script>
export default {
  methods: {
    goToShop() {
      this.$router.push("/AdminShop");
    },
    goToOrder() {
      this.$router.push("/Reserve");
    },
    goToEdit() {
      this.$router.push("/Edit");
    },
  },
};
</script>
