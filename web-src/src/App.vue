<script setup>
import { ref } from 'vue';
const greeting = ref("")

const update_greeting = (_greeting) => {
  greeting.value = _greeting
}
const click = () => {
  eel.get_greeting("user")(update_greeting)
  eel.hello_world()
  console.log("clicked")
}

let onBegin = () => {
  console.log('=== Begin ===');
}

let onEnd = () => {
  console.log('=== End ===');
}


</script>

<template>
  <div>
    <p>{{ greeting }}</p>
    <button type="button" @click="click()">Click me</button>
  </div>
  <div id="app">
    <VueSignaturePad
      width="500px"
      height="500px"
      ref="signaturePad"
      :options="{ onBegin, onEnd }"
    />
  </div>

  <div class="menubutton">
    Löschen
  </div>
  <div class="menubutton" >
    Zurück
  </div>
  <div class="menubutton" > 
    Abschicken
  </div>



</template>
