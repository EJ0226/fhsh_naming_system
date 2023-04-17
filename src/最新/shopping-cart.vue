<script>
import CartProduct from "../components/Cart-Product.vue";
import QuantityPlusMinus from "../components/Quantity-plus-minus.vue";

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
    goto() {
      this.$router.push("/");
    },
  },
};
</script>

<template>
  <div class="overflow-x-hidden">
    <div class="relative w-screen overflow-x-hidden">
      <!-- Gray block title -->
      <div class="w-full h-[6vw] bg-[#F28383] flex justify-center items-center">
        <p class="font-bold text-[3vw] text-white">MY CART</p>
      </div>

      <div>
        <CartProduct class="mt-[5vw]" />

        <CartProduct />
      </div>

      <!-- Bottom gray block (total price, checkout) -->
      <footer>
        <div
          class="w-full h-[15vw] bg-[#F28383] mt-[4vw] flex justify-center items-center"
        >
          <p class="font-black text-[3vw] pr-[35vw] text-white">總金額＄</p>
          <button
            @click="goto"
            class="w-[16vw] h-[6vw] bg-[#FFFFFF] font-black text-[3vw]"
          >
            下單
          </button>
        </div>
      </footer>
    </div>
  </div>
</template>
