<template>
  <div class="max-w-screen h-full">
    <div class="w-full h-[60px] bg-[#D9D9D9]">
      <h1 class="text-[36px] text-center font-thin">商品新增</h1>
    </div>
      <div>
        <form @submit.prevent="create">
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label for="name" class="ml-[10px] font-bold">商品名稱:</label>
            <input
              maxlength="20"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
              placeholder="請輸入商品名稱"
              id="name"
              name="name"
              v-model="formData.name"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label for="price" class="ml-[10px] font-bold">商品價格:</label>
            <input
              placeholder="請輸入商品價格(單位為NT)"
              minlength="0"
              type="number"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
              id="price"
              name="price"
              v-model="formData.price"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label for="quatity" class="ml-[10px] font-bold">商品數量:</label>
            <input
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"  
              placeholder="請輸入商品數量"
              minlength="0"
              type="number"
              id="quatity"
              name="quatity"
              v-model="formData.quantity"
            />
          </div>
          <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
            <label for="summary" class="ml-[10px] font-bold">商品敘述: </label>
            <input
              placeholder="請輸入商品敘述"
              id="summary"
              name="summary"
              v-model="formData.summary" 
              maxlength="100"
              class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
            />
          </div>
          <button 
          type="submit"
          class="border-2 border-[#000000] text-[20px] font-bold text-center w-[100px] h-[40px]"
        >
          上架
        </button>
        </form>
      </div>
    </div>
    <div class="w-full">
      <div class="w-full flex justify-evenly items-center mt-[10px]">
      </div>
    </div>
</template>


<script setup>
import axios from "axios"; 
import { ref, reactive } from "vue"; //引入
import { useRouter } from "vue-router"
const request = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
})

    const formData = reactive({ //設定資料
      name: "",
      summary: "",
      quantity: "",
      price: "",
    });
    const router = useRouter()

  const create = () => {
    const data = { 
      name: formData.name,
      summary: formData.summary,
      quantity: formData.quantity,
      price: formData.price,
    }
    request.post("/create_item", data)
        .then(response => {
          router.push("/Admin");
          console.log(response.data)
        })
        .catch(error => {
          console.log(error.response.data)
        })
      }
  const goToShop = () => {
    console.log(data)
        router.push("/Admin");
        }
</script>

<!-- <style>
.image-list {
  display: flex;
  flex-wrap: wrap;
}

.image-item {
  flex: 1;
  margin: 5px;
}
</style> -->
