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
  <div
    class="overflow-x-hidden mt-[10vw] flex items-center justify-center flex-col"
  >
    <div
      class="w-[40vw] h-[23vw] min-w-[20vw] min-h-[10vw] bg-[#F28383] bg-opacity-40 rounded-[2vw] border-[0.13vw] border-black overflow-x-hidden flex justify-center items-center"
    >
      <div
        class="w-[18vw] h-[18vw] bg-[#FFFFFF] bg-opacity-60 border-[0.13vw] border-black rounded-[2vw] overflow-x-hidden text-center flex flex-col justify-center items-center"
      >
        <p
          class="text-[2.4vw] font-black text-center mt-[1vw] whitespace-nowrap"
        >
          您的商品<br />已成功預購
        </p>
        <p class="text-[1.4vw] text-center mt-[2vw] whitespace-nowrap">
          請 匯 款 到 此 帳 戶<br />( )
        </p>
      </div>
      <img src="../assets/Ok.png" alt="ok" class="w-[17vw] h-[17vw] ml-[1vw]" />
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
