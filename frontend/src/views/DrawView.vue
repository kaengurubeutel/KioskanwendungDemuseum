<script setup lang="ts">
import { ref } from 'vue'
import CusButton from '@/components/CusButton.vue'
const signaturePad = ref()
import { useRouter } from 'vue-router'
import { imagestore } from '@/stores/imagestore'

const imgStore = imagestore();

const route = useRouter()

// The `undo` function is a callback function that is triggered when the "undo" button is clicked. It
// calls the `undoSignature` method on the `signaturePad` ref object. This method is responsible for
// undoing the last stroke or action made on the signature pad, effectively removing the most recent
// signature.
let undo = () => {
  signaturePad.value.undoSignature()
}

// The `clear` function is a callback function that is triggered when the "delete" button is clicked.
// It calls the `clearSignature` method on the `signaturePad` ref object, which clears the signature on
// the signature pad.
let clear = () => {
  signaturePad.value.clearSignature()
}

// The `save` function is a callback function that is triggered when the "send" button is clicked.
let save = () => {
  //TODO
  const { isEmpty, data } = signaturePad.value.saveSignature()
  console.log(isEmpty)
  console.log(data)
  //let response = eel.get_image(data)
  imgStore.scribble=data;

  route.push({ path: 'prompt' })
}
</script>

<template>
  <main>
    <div id="background"></div>
    <div id="drwWrp">
      <VueSignaturePad
        id="sig"
        width="1500px"
        height="800px"
        ref="signaturePad"
        :options="{ onBegin, onEnd, backgroundColor: '#FFF', minWidth: 1.3, maxWidth: 3.3 }"
      />
    </div>

    <div id="menu">
      <CusButton text="undo" @click="undo"></CusButton>
      <CusButton text="delete" @click="clear"></CusButton>
      <CusButton text="send" @click="save"></CusButton>
    </div>
  </main>
</template>

<style scoped>
#background {
  z-index: 0;
  background-color: var(--orange);
  position: absolute;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
}
#drwWrp {
  position: relative;
  width: 1505px;
  height: 805px;
  z-index: 4;

  border: 2.5px solid #000;
  background: #fff;
  /* Schatten 1 */
  box-shadow: 2px 4px 0px 0px #161617;
}

#menu {
  position: relative;
  z-index: 3;
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
  gap: 70px;
}

main {
  position: absolute;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
