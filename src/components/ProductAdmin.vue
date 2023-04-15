<script setup>
import minusSvg from "../assets/Minus.svg";
import editSvg from "../assets/Edit.svg";

const props = defineProps(["product", "price"]);
</script>

<template>
  <div class="flex justify-center items-center">
    <div class="h-[200px] w-[200px] border-2 border-[#000000]"></div>

    <div class="ml-[40px]">
      <p class="">
        {{ product }}
      </p>
      <p class="mt-[30px]">${{ price }}</p>
      <button
        class="rounded-[10px] w-[80px] h-[30px] bg-[#ffffff] font-black mt-[30px] shadow-2xl border-2 border-[#D9D9D9]"
        @click="goToMaterial"
      >
        VIEW
      </button>
      <div class="flex mt-[20px] justify-evenly">
        <button
          class="w-[40px] h-[40px] rounded-[40px] border-2 border-[#000000] flex justify-center items-center"
        >
          <img :src="minusSvg" alt="minusSvg" class="w-[20px] h-[20px]" />
        </button>
        <button
          @click="goToEdit"
          class="w-[40px] h-[40px] rounded-[40px] border-2 border-[#000000] flex justify-center items-center ml-[10px]"
        >
          <img :src="editSvg" alt="editSvg" class="w-[20px] h-[20px]" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goToEdit() {
      this.$router.push("/Edit");
    },
    goToMaterial() {
      this.$router.push("/Material");
    },
  },
};
</script>
