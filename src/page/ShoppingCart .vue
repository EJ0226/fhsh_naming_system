<script setup>
import CartProduct from "../components/Cart-Product.vue";
import QuantityPlusMinus from "../components/Quantity-plus-minus.vue";
</script>

<!--<template>
  <div class="w-full min-h-screen">
   
    <div
      class="w-full h-16 sm:h-20 md:h-24 bg-gray-300 flex justify-center items-center"
    >
      <p class="font-black text-2xl sm:text-3xl md:text-4xl">MY CART</p>
    </div>

    
    <div class="w-full h-6 sm:h-8 md:h-10 bg-white"></div>

    <div class="w-full h-full mt-5">
      <CartProduct />
      <br />
      <CartProduct />
    </div>

    <div class="w-full h-16 sm:h-20 md:h-24 bg-white"></div>

    
    <div
      class="w-full h-50 sm:h-60 md:h-70 bg-gray-300 flex justify-center items-center"
    >
      <p
        class="font-black text-2xl sm:text-3xl md:text-4xl mr-2 sm:mr-4 md:mr-6"
      >
        總金額＄
      </p>
      <button
        class="w-60 sm:w-55 md:w-85 h-20 sm:h-20 md:h-28 bg-white font-black text-lg sm:text-xl md:text-2xl"
      >
        下單
      </button>
    </div>
    <product-page @add-to-cart="handleAddToCart"></product-page>
  </div>
</template>-->

<template>
  <div class="overflow-x-hidden">
    <div class="relative w-screen overflow-x-hidden">
      <!-- Gray block title -->
      <div
        class="w-full h-[12vw] bg-[#D9D9D9] flex justify-center items-center"
      >
        <p class="font-bold text-[4vw]">MY CART</p>
      </div>

      <div>
        <CartProduct class="mt-[5vw]" />

        <CartProduct />
      </div>

      <!-- Bottom gray block (total price, checkout) -->
      <footer>
        <div
          class="w-full h-[35vw] bg-[#D9D9D9] flex justify-center items-center"
        >
          <p class="font-black text-[4vw] pr-[35vw]">總金額＄</p>
          <button
            @click="gotoconfirmpurchase"
            class="w-[28vw] h-[12vw] bg-[#FFFFFF] font-black text-[4vw]"
          >
            下單
          </button>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    CartProduct,
    QuantityPlusMinus,
  },
  data() {
    return {
      products: [], // 存儲商品信息
      name: "Product 1",
      price: 100,
      quantity: 1,
    };
  },
  methods: {
    handleAddToCart(products) {
      // 接收來自product-page.vue的數據
      console.log(products);
    },
    addToCart() {
      // 將商品信息添加到products陣列中
      this.products.push({
        name: this.name,
        price: this.price,
        quantity: this.quantity,
      });

      // 觸發自定義事件，並將數據作為參數傳遞
      this.$emit("add-to-cart", this.products);
    },
    gotoconfirmpurchase() {
      this.$router.push("/confirmpurchase");
    },
  },
};
</script>
