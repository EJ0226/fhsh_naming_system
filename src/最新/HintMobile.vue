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
      class="w-[50vw] h-[65vw] min-w-[20vw] min-h-[10vw] bg-[#F28383] bg-opacity-40 rounded-[2vw] border-[0.13vw] border-black overflow-x-hidden flex justify-center items-center"
    >
      <div
        class="w-[43vw] h-[58vw] bg-[#FFFFFF] bg-opacity-60 border-[0.13vw] border-black rounded-[2vw] overflow-x-hidden flex flex-col justify-center items-center"
      >
        <img
          src="../assets/Ok.png"
          alt="ok"
          class="w-[17vw] h-[17vw] mt-[2vw]"
        />
        <p class="text-[2vw] font-black text-center mt-[1vw] whitespace-nowrap">
          您的商品<br />已成功預購
        </p>
        <p class="text-[0.1vw] text-center mt-[2vw] whitespace-nowrap">
          請 匯 款 到 此 帳 戶<br />( )
        </p>
      </div>
    </div>
    <button
      @click="gotoshopuser"
      class="text-[0.5vw] w-[11vw] h-[5.5vw] bg-[#F28383] rounded-[1.2vw] text-white flex justify-center items-center mt-[3vw]"
    >
      確認
    </button>
    <div
      class="w-full h-[4vw] bg-[#F28383] mt-[7vw] text-white flex justify-center items-center text-[1vw]"
    >
      校址：112056臺北市北投區復興四路70號 <br />
      電話：02-28914131 傳真：02-28952156
    </div>
  </div>
</template>
