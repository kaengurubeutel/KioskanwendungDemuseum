<script setup lang="ts">
import LoadingAnim from '@/components/LoadingAnim.vue'
import FailScreen from '@/components/FailScreen.vue'
import ResultScreen from '@/components/ResultScreen.vue';
import { imagestore } from '@/stores/imagestore'
import { ref, onMounted } from 'vue';

const imgStore = imagestore();
const state = ref(0);

const sendImg =  async () => {
  let result = await eel.get_image(imgStore.scribble, imgStore.promptdata.prompt, imgStore.promptdata.guidance_scale);
  console.log(result)
  return true;
}

onMounted(()=>{
  sendImg();
})

</script>

<template>
  <div id="wrapper">
    <LoadingAnim v-if="state===0"></LoadingAnim>
    <FailScreen v-if="state===1"></FailScreen>
    <ResultView v-if="state===2"></ResultView>
   
  </div>
</template>

<style scoped>
#wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  background: #ff8a1e;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 5;
}
</style>
