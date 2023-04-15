<script setup>
const props = defineProps(["text"]);
</script>

<template>
  <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
    <label class="ml-[10px] font-bold">{{ text }}</label>
    <input class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]" />
  </div>
</template>
