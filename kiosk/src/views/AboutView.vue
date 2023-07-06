<script setup lang="ts">

import { ref } from 'vue';

const signaturePad = ref();

let onBegin = () => {
  console.log('=== Begin ===');
}

let onEnd = () => {
  console.log('=== End ===');
}

let undo = () => {
        signaturePad.value.undoSignature();
}

let clear = () => {
  signaturePad.value.clearSignature();
}

let save = () => {
  const { isEmpty, data } = signaturePad.value.saveSignature();
  console.log(isEmpty);
  console.log(data);
  let response = eel.get_image(data);
  console.log(response);
}


</script>


<template>
   <div id="about">
        <VueSignaturePad
          id="sig"
          width="500px"
          height="500px"
          ref="signaturePad"
          :options="{ onBegin, onEnd, backgroundColor: '#FFF', minWidth:1.3, maxWidth:3.3}"
        />
   
      <div id="menuwrapper">
           <div class="menubutton" @click="clear">
            Löschen
          </div>
          <div class="menubutton" @click="undo" >
            Zurück
          </div>
          <div class="menubutton" @click="save" > 
            Abschicken
        </div>
      </div>
    </div>

      
</template>

<style>

.menubutton{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
  margin: 10px;
  width: 100px;
  height: 40px;
  border-radius: 9px;
  border: 1px solid #fff;
}

.menubutton:hover{
  background-color: rgba(248, 248, 248, 0.10);
}

.menubutton:active{
  box-shadow: 0px 0px 10px 0px rgba(227, 227, 227, 0.25);
}

#menuwrapper{
  margin-top: 30px;
  display: flex;
  flex-direction: row;

}

#sig{
  background-color: #fff;
  border: 1px solid #fff;
}

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
