<script setup>
const props = defineProps(["product", "quantity"]);
</script>

<template>
  <div class="w-full h-full">
    <div class="flex mt-[5px] ml-[10px]">
      <p>商品名稱 {{ product }}</p>
      <p class="ml-[10px]">數量 {{ quantity }}</p>
    </div>
  </div>
</template>
