<script>
export default {
  methods: {
    gotoshopuser() {
      this.$router.push("/shopuser");
    },
  },
};
</script>
<template>
  <div class="overflow-x-hidden flex items-center justify-center flex-col">
    <div
      class="w-[40vw] h-[23vw] bg-[#F28383] bg-opacity-40 rounded-[2vw] border-[0.13vw] border-black flex justify-center items-center mt-[10vw]"
    >
      <div
        class="w-[28vw] h-[16vw] bg-[#FFFFFF] bg-opacity-60 rounded-[2vw] border-[0.15vw] border-black flex flex-col justify-center items-center"
      >
        <p class="text-[2vw] font-black text-center">您的商品<br />預購失敗</p>
      </div>
    </div>
    <button
      @click="gotoshopuser"
      class="text-[1.8vw] w-[9vw] h-[3.5vw] bg-[#F28383] rounded-[1.2vw] text-white flex justify-center items-center mt-[3vw]"
    >
      確認
    </button>
    <div
      class="w-full h-[4vw] bg-[#F28383] mt-[7vw] text-white flex justify-center items-center text-[1.1vw]"
    >
      校址：112056臺北市北投區復興四路70號 <br />
      電話：02-28914131 傳真：02-28952156
    </div>
  </div>
</template>
