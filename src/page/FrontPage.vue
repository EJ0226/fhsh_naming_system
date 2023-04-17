<template>
  <div class="max-w-screen">
    <div class="w-full h-[50px] bg-[#657099] flex">
      <img
        :src="searchSvg"
        alt="searchSvg"
        class="w-[30px] h-[30px] mt-[10px] ml-[10px]"
      />
      <input
        class="w-[200px] h-[30px] mt-[10px] rounded-[10px] ml-[10px]"
        placeholder="搜尋想查找的商品"
        type="text"
        required
        maxlength="50"
        @keyup.enter="search"
        v-model="searchKeyword"
      />
      <label>選擇查詢時的排序方式</label>
      <select v-model="sort_by">
        <option value="price_desc">選擇以價格降序排序</option>
        <option value="price_asc">選擇以價格升序排序</option>
        <option value="searchKeyword_desc">選擇以名稱降序排序</option>
        <option value="searchKeyword_asc">選擇以名稱升序排序</option>
      </select>
      <button
        @click="goToLogin"
        class="w-[70px] h-[30px] bg-[#ffffff] ml-[10px] mt-[10px] rounded-[10px]"
      >
        登入
      </button>
    </div>
    <button @click="previousPage">上一頁</button>
    <span>目前頁數：{{ Page }}</span>
    <button @click="nextPage">下一頁</button>
    <div
      class="w-full h-[150px] bg-[#657099] mt-[25px] flex justify-center items-center"
    >
      <p class="font-black text-[40px] text-[#ffffff]">FHSH MARKET</p>
    </div>
    <div
      class="w-full mt-[25px] grid grid-cols-1 md:grid-cols-2 items-center justify-self-center gap-2 gap-y-8"
    >
      <Product
        v-for="product in products"
        :key="product.productName"
        :product="product.productName"
        :price="product.price"
      />
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import searchSvg from "../assets/Search.svg";
import Product from "../components/ProductUser.vue";
//把後端儲存好的商品資料顯示在網頁上(粗略)
const Page = ref(1); // 當前頁數
const products = ref([]); // 當前頁面顯示的商品資料
const searchKeyword = ""; // 搜尋關鍵字
const sort_by = "price_desc"; //預設使用者選擇以價格降序排序
const fetchData = async () => {
  const data = {
    Page: Page.value,
    searchKeyword: searchKeyword.value,
    sort_by: sort_by.value,
  };
  const response = await axios.get(`/api/products`, data);
  products.value = response.data;
};

const nextPage = () => {
  currentPage.value += 1;
  fetchData();
};
const goToLogin = () => {
  router.push("/login");
};
const goToRegist = () => {
  router.push("/regist");
};
</script>
