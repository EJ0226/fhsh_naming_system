<template>
  <div>
    <div class="w-screen h-[50px] bg-[#D9D9D9] flex">
      <button @click="goToEdit" class="ml-auto">
        <img :src="plusSvg" alt="plusSvg" class="w-[40px] h-[40px]" />
      </button>
    </div>
    <div class="my-[10px]">
      <p class="text-center text-[36px] font-bold">Admin</p>
    </div>
    <div class="w-screen h-[3px] bg-[#D9D9D9]"></div>
    <div class="flex justify-evenly mt-[20px]">
      <button
        @click="goToShop"
        class="w-[130px] h-[130px] bg-[#D9D9D9] font-bold text-[20px]"
      >
        瀏覽商品
      </button>
      <button
        @click="goToOrder"
        class="w-[130px] h-[130px] bg-[#D9D9D9] font-bold text-[20px]"
      >
        訂單查詢
      </button>
    </div>
  </div>
</template>
<!--管理者登入後可以進行操作的總頁面
ex:瀏覽商品 新增/修改商品 查看訂單-->
<script setup>
import plusSvg from "../assets/Plus.svg";
//axios function
//希望有甚麼公
goToShop = () => {
  $router.push("/shopAdmin");
};
goToOrder = () => {
  router.push("/Reserve");
};
goToEdit = () => {
  router.push("/Edit");
};
</script>
