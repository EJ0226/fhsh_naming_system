<script setup>
const props = defineProps(["product", "price"]);
</script>

<template>
  <div class="flex justify-center items-center bg-[#A5ADC7] rounded-[5px]">
    <div
      class="h-[200px] w-[200px] border-2 border-[#000000] rounded-[10px] m-[10px]"
    ></div>
    <div class="ml-[40px]">
      <p class="mt-[30px]">
        {{ product }}
      </p>
      <p class="mt-[30px]">${{ price }}</p>
      <button
        class="rounded-[10px] w-[80px] h-[30px] bg-[#ffffff] font-black mt-[30px] border-2 border-[#D9D9D9]"
        @click="goToMaterial"
      >
        VIEW
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToMaterial() {
      this.$router.push("/Material");
    },
  },
};
</script>
