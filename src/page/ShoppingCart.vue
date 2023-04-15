<script setup>
import CartProduct from "../components/Cart-Product.vue";
</script>

<template>
  <div class="w-full min-h-screen">
    <!-- Gray block title -->
    <div
      class="w-full h-16 sm:h-20 md:h-24 bg-gray-300 flex justify-center items-center"
    >
      <p class="font-black text-2xl sm:text-3xl md:text-4xl">MY CART</p>
    </div>

    <!-- Space between title and component -->
    <div class="w-full h-6 sm:h-8 md:h-10 bg-white"></div>

    <div class="w-full h-full mt-5">
      <CartProduct />
      <br />
      <CartProduct />
    </div>

    <div class="w-full h-16 sm:h-20 md:h-24 bg-white"></div>

    <!-- Bottom gray block (total price, checkout) -->
    <div
      class="w-full h-50 sm:h-60 md:h-70 bg-gray-300 flex justify-center items-center"
    >
      <p
        class="font-black text-2xl sm:text-3xl md:text-4xl mr-2 sm:mr-4 md:mr-6"
      >
        總金額＄
      </p>
      <button
        class="w-60 sm:w-55 md:w-85 h-20 sm:h-20 md:h-28 bg-white font-black text-lg sm:text-xl md:text-2xl"
      >
        下單
      </button>
    </div>
  </div>
</template>

<!-- <script setup>
import CartProduct from "../components/Cart-Product.vue";
</script>

<template>
  <div class="w-screen h-screen">
     灰色區塊標題 
    <div
      class="w-screen h-[60px] bg-[#D9D9D9] flex justify-center items-center"
    >
      <p class="font-black text-[28px]">MY CART</p>
    </div>

 標題與component之間空隙 
    <div class="w-screen h-[30px] bg-[#FFFFFF]"></div>

    <div class="w-screen h-full mt-[25px]">
      <CartProduct />
    </div>

    <div class="w-screen h-[40px] bg-[#FFFFFF]"></div>

  下方灰色區塊（總金額、下單） 
    <div
      class="w-screen h-[180px] bg-[#D9D9D9] flex justify-center items-center"
    >
      <p class="font-black text-[28px] mx-[140px]">總金額＄</p>
      <button
        class="w-[260px] h-[84px] bg-[#FFFFFF] font-black text-[25px] mx-[140px]"
      >
        x 下單
      </button>
    </div>
  </div>
</template> -->
