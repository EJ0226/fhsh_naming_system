<script setup>
import searchSvg from "../assets/magnifying-glass-solid.svg";
import shoppingcartSvg from "../assets/cart-shopping-solid.svg";
import Product from "../components/Product.vue";

const products = [
  { productName: "帽踢", price: "650" },
  { productName: "書包", price: "690" },
  { productName: "棒球外套", price: "1080" },
  { productName: "帆布袋", price: "235" },
];
</script>
<template>
  <div class="relative w-screen overflow-x-hidden flex flex-col items-center">
    <div class="w-full h-[6vw] bg-[#F28383] flex items-center">
      <button>
        <img
          :src="searchSvg"
          alt="searchSvg"
          class="w-[40px] h-[40px] ml-[2vw]"
        />
      </button>
      <input
        class="w-[50vw] h-[4vw] border-[0.5vw] ml-[1.5vw] border-white rounded-[0.8vw] text-[2vw] text-center"
        placeholder="搜尋想查找的商品"
      />
      <button class="ml-auto">
        <img
          :src="shoppingcartSvg"
          aly="shoppingcartSvg"
          class="w-[40px] h-[40px] mr-[2vw]"
        />
      </button>
    </div>
    <div
      class="w-full h-[30vw] bg-[#F28383] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div
      class="items-center mt-[4vw] ml-[2vw] grid grid-cols-2 grid-rows-2 gap-[6vw]"
    >
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
