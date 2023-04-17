<script setup>
const props = defineProps(["product", "price"]);
</script>

<template>
  <div class="flex justify-center items-center">
    <div class="h-[200px] w-[200px] border-2 border-[#000000]"></div>
    <div
      class="ml-[40px]"
      v-for="product in filteredProducts"
      :key="product.id"
    >
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
