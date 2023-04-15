<script setup>
import { ref } from "vue";
import QuantityPlusMinus from "./Quantity-plus-minus.vue";
</script>

<template>
  <div class="flex justify-center items-center">
    <div class="max-w-screen h-[250px] bg-[#D9D9D9] flex items-center">
      <label class="flex items-center">
        <input type="checkbox" class="form-checkbox h-5 w-5 ml-[30px]" />
      </label>
      <div class="w-[300px] h-[200px] bg-[#FFFFFF] ml-[20px]"></div>
      <p class="font-black text-[20px] text-black ml-[25px] mt-[-120px]">
        PRODUCT 1
      </p>
      <p class="font-black text-[28px] text-black ml-[-160px]">$</p>
      <p class="font-blod text-[28px] text-black ml-[100px]">x</p>
      <div
        class="border-2 border-[#000000] text-[20px] font-bold text-center w-[150px] h-[50px] ml-[-135px] mt-[140px] flex items-center"
      >
        <QuantityPlusMinus class="ml-[20px]" />
      </div>
    </div>
  </div>
</template>
