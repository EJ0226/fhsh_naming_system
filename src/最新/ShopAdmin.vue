<script setup>
import searchSvg from "../assets/magnifying-glass-solid.svg";
import Product from "../components/ProductEdit.vue";

const products = [
  { productName: "帽踢", price: "650" },
  { productName: "書包", price: "690" },
  { productName: "棒球外套", price: "1080" },
  { productName: "帆布袋", price: "235" },
];
</script>
<template>
  <div class="relative w-screen overflow-x-hidden flex flex-col items-center">
    <div class="w-full h-[50px] bg-[#F28383] flex">
      <button>
        <img :src="searchSvg" alt="searchSvg" class="w-[40px] h-[40px]" />
      </button>
      <div
        class="w-[55vw] h-[5vw] border-[0.5vw] mt-[0.65vw] ml-[2vw] border-white rounded-[1vw]"
      ></div>
    </div>
    <div
      class="w-full h-[30vw] bg-[#F28383] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div class="flex flex-col items-center mt-[25px]">
      <Product
        v-for="product in products"
        :key="product.productName"
        :product="product.productName"
        :price="product.price"
      />
    </div>
    <div
      class="w-full h-[10vw] bg-[#F28383] mt-[20vw] text-white flex justify-center items-center text-[2.2vw]"
    >
      校址：112056臺北市北投區復興四路70號 <br />
      電話：02-28914131 傳真：02-28952156
    </div>
  </div>
</template>
