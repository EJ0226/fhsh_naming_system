<template>
  <div class="h-screen bg-[#FFFAF0]">
    <div class="flex justify-between">
      <div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-32"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-28"></div>
        <div class="p-2"></div>
        <div class="border-t-4 rounded-full border-[#97AEB9] w-24"></div>
      </div>
      <div
        class="text-right text-[#97AEB9] font-semibold text-md leading-9 pr-7"
      >
        <div class="p-1"></div>
        復興高中<br />自主學習點名系統
      </div>
    </div>

    <div class="flex flex-col justify-center items-center">
      <div class="p-12"></div>
      <div class="bg-[#D9D9D9] w-64 h-44"></div>

      <div class="flex justify-center items-center gap-8 pt-10">
        <!-- 重拍 -->
        <a>
          <button>
            <span
              class="button font-semibold text-xl rounded-md text-[#97aeb9] text-center bg-white px-5 py-4"
              >重拍</span
            >
          </button>
        </a>

        <!-- 確定 -->
        <a>
          <button>
            <span
              class="button font-semibold text-xl rounded-md text-white text-center bg-[#97aeb9] px-5 py-4"
            >
              確定
            </span>
          </button>
        </a>
      </div>
      <div class="p-12"></div>
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
.button {
  box-shadow: 1px 1px 4px 0px rgba(0, 0, 0, 0.25);
}
</style>
