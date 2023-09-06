<script setup lang="ts">
import LoadingAnim from '@/components/LoadingAnim.vue'
import FailScreen from '@/components/FailScreen.vue'
import ResultScreen from '@/components/ResultScreen.vue';
import { imagestore } from '@/stores/imagestore'
import { ref, onMounted } from 'vue';

const imgStore = imagestore();
const state = ref(0);


const sendImg =   () => {
  eel.get_image(imgStore.scribble, imgStore.promptdata.prompt, imgStore.promptdata.guidance_scale);
  return true;
}

eel.expose(callback, "result_callback")
function callback(failure:boolean, image){
  if(!failure){
    console.log(image)
    imgStore.result = image;
    state.value = 2;
  } else{
    state.value = 1;
  }

}

onMounted(()=>{
  sendImg();
})

</script>

<template>
  <div id="wrapper">
    <LoadingAnim v-if="state===0"></LoadingAnim>
    <FailScreen v-if="state===1"></FailScreen>
    <ResultScreen v-if="state===2"></ResultScreen>
   
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
