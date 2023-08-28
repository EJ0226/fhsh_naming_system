<template>
  <div class="bg-[#FAF7EF] h-screen">
    <div class="flex justify-between">
      <div>
        <div class="p-4"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      </div>
      <div
        class="text-right text-[#97AEB9] font-semibold text-md leading-9 pr-7"
      >
        <div class="p-3"></div>
        復興高中<br />自主學習點名系統
      </div>
    </div>

    <div class="flex justify-center items-center">
      <div class="py-56"></div>
      <div
        class="bg-[#FFFFFF] py-20 px-16 rounded-xl custom-shadow text-center"
      >
        <span class="text-[#3D3D3D] font-bold text-3xl text-center"
          >點名成功！</span
        >
        <div class="pt-8"></div>

        <a
          ><button
            class="rounded-lg px-8 py-2 bg-[#698694] border border-[#698694]"
          >
            <span class="text-white text-lg font-medium">確定</span>
          </button></a
        >
      </div>
    </div>
    <div class="absolute flex flex-col items-end right-0">
      <div class="p-6"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      <div class="p-2"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
      <div class="p-2"></div>
      <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
    </div>
  </div>
</template>

<style>
.custom-shadow {
  box-shadow: 2px -2px 4px 0px rgba(0, 0, 0, 0.25) inset,
    2px 2px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>
