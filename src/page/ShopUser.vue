<template>
  <div class="max-w-screen">
    <div class="w-full h-[50px] bg-[#D9D9D9] flex">
      <img
        :src="searchSvg"
        alt="searchSvg"
        class="w-[30px] h-[30px] mt-[10px] ml-[10px]"
      />
      <input
        class="w-[200px] h-[30px] mt-[10px] rounded-[10px] ml-[10px]"
        placeholder="搜尋想查找的商品"
      />
      <button
        class="w-[30px] h-[30px] mt-[10px] ml-auto"
        @click="goToShoppingCart"
      >
        <img :src="shoppingcartSvg" alt="shoppingcartSvg" />
      </button>
    </div>
    <div
      class="w-full h-[150px] bg-[#D9D9D9] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div
      class="w-full mt-[25px] grid grid-cols-1 md:grid-cols-2 items-center justify-self-center gap-2 gap-y-8"
    >
      <Product
        v-for="product in products"
        :key="product.productName"
        :product="product.productName"
        :price="product.price"
      />
    </div>
  </div>
</template>

<script setup>
import searchSvg from "../assets/Search.svg";
import { useRouter } from "vue-router";
import shoppingcartSvg from "../assets/ShoppingCart.svg";
import Product from "../components/ProductUser.vue";
import { reactive } from "vue";
const products = reactive([]); //商品
const router = useRouter();
    goToShoppingCart = () => {
      router.push("/shoppingCart");
    },
</script>
