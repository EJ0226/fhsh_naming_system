<template>
  <div class="max-w-screen h-full">
    <div class="w-full h-[60px] bg-[#D9D9D9]">
      <p class="text-[36px] text-center font-thin">商品新增</p>
    </div>
    <div class="ml-[15px]">
      <!-- <img />
      <div class="mt-[20px]">
        <input type="file" ref="fileInput" multiple @change="handleFileInput" />
        <div v-if="imageDataUrls.length" class="image-list">
          <div
            v-for="(imageUrl, index) in imageDataUrls"
            :key="index"
            class="image-item"
          >
            <img
              :src="imageUrl"
              :style="{
                maxWidth: '100px',
                maxHeight: '100px',
              }"
            />
          </div>
        </div>
      </div> -->

      <div>
        <form @submit.prevent="create">
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label class="ml-[10px] font-bold">商品名稱:</label>
            <input
              v-model="formdata.name"
              maxlength="20"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label class="ml-[10px] font-bold">商品價格$(NT):</label>
            <input
              v-model="formdata.price"
              minlength="0"
              type="number"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label class="ml-[10px] font-bold">商品數量:</label>
            <input
              v-model="formdata.quantity"
              minlength="0"
              type="number"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label class="ml-[10px] font-bold">商品敘述: </label>
            <input
              v-model="formdata.summary"
              maxlength="100"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
            />
          </div>
        </form>
      </div>
    </div>
    <div class="w-full">
      <div class="w-full flex justify-evenly items-center mt-[10px]">
        <button
          type="submit"
          class="border-2 border-[#000000] text-[20px] font-bold text-center w-[100px] h-[40px]"
        >
          上架
        </button>
      </div>
    </div>
  </div>
</template>

<!--新增商品資料-->
<script setup>
import axios from "axios";
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
//能將商品資料的form成功cosole並傳入後端資料庫
const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

const formdata = reactive({
  //設定資料
  name: "",
  summary: "",
  quantity: "",
  price: "",
});
const router = useRouter();
//開始建立axios
const create = () => {
  //先接收資料
  const data = {
    name: formdata.name,
    summary: formdata.summary,
    quantity: formdata.quantity,
    price: formdata.price,
  };
  //變數.method("後端提供的url  ")
  instance
    .post("/create_item", data)
    .then((response) => {
      //router放這裡
      router.push("/Admin");
      console.log(response.data); //打印出回傳的東西
    })
    .catch((error) => {
      console.log(error.response.data);
    });
};
const goToShop = () => {
  router.push("/Admin");
};
</script>

<style>
.image-list {
  display: flex;
  flex-wrap: wrap;
}

.image-item {
  flex: 1;
  margin: 5px;
}
</style>
