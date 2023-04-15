<template>
  <!-- <div class="max-w-screen h-full relative">
    <div class="w-full h-[60px] bg-[#D9D9D9]"> -->
      <p class="text-[36px] text-center font-thin">商品修改</p>
    <!-- </div>
    <div class="ml-[15px]">
      <img />
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
      </div>

      <div>
        <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
          <label class="ml-[10px] font-bold">商品名稱:</label>
          <input
            v-model="name"
            maxlength="20"
            class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
          />
        </div>
        <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
          <label class="ml-[10px] font-bold price">商品價格$(NT):</label>
          <input
            v-model="price"
            minlength="0"
            type="number"
            class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
          />
        </div>
        <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
          <label class="ml-[10px] font-bold quqntity">商品數量:</label>
          <input
            v-model="quqntity"
            minlength="0"
            type="number"
            class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
          />
        </div>
        <div class="w-[290px] h-[70px] bg-[#D9D9D9] mt-[20px]">
          <label class="ml-[10px] font-bold category">商品敘述: </label>
          <input
            v-model="about"
            maxlength="100"
            class="border-2 border-[#D9D9D9] w-[270px] h-[35px] ml-[10px]"
          />
        </div>
      </div>
    </div>

    <div class="w-full">
      <div class="w-full flex justify-evenly items-center mt-[30px]">
        <button
          type="submit"
          class="border-2 border-[#000000] text-[20px] font-bold text-center w-[100px] h-[40px]"
        >
          儲存
        </button>
      </div>
    </div>
  </div> -->
</template>

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

<!-- <script setup>
// import axios from "axios";

// axios
//   .get("http://localhost:8000/items")
//   .then((response) => console.log(response.data))
//   .catch((error) => console.error(error));

    handleFileInput = () => {
      const files = this.$refs.fileInput.files;
      if (!files.length) return;

      for (let i = 0; i < files.length; i++) {
        const file = files[i];

        // 驗證文件類型是否為圖片
        if (!/^image\//.test(file.type)) {
          alert("只能上傳圖片");
          return;
        }

        // 讀取文件內容，轉換為 Data URL 格式，用於顯示圖片
        const reader = new FileReader();
        reader.onload = () => {
          this.imageDataUrls.push(reader.result);
        };
        reader.readAsDataURL(file);
      }
};
</script> -->
