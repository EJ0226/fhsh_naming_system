<script setup>
import Material from "./Material.vue";

const props = defineProps(["num", "name", "number"]);

const materials = [
  { product: "帽踢", quantity: "2" },
  { product: "書包", quantity: "1" },
];
</script>

<template>
  <div
    class="h-full max-w-[300px] bg-[#D9D9D9] rounded-[10px] ml-[10px] mt-[20px]"
  >
    <div class="font-bold mt-[10px] ml-[10px]">訂單編號 {{ num }}</div>
    <div class="font-bold mt-[10px] ml-[10px]">訂單者姓名 {{ name }}</div>
    <div class="font-bold mt-[10px] ml-[10px]">匯款帳號後五碼 {{ number }}</div>
    <div>
      <Material
        v-for="material in materials"
        :key="material.product"
        :product="material.product"
        :quantity="material.quantity"
      />
    </div>
  </div>
</template>
