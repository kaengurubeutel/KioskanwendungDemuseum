<script setup lang="ts">
import SimpleKeyboard from '../components/SimpleKeyboard.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { imagestore } from '@/stores/imagestore'

const imgStore = imagestore();
const route = useRouter()
const text = ref('')

const swButtons = ref([0, 0, 1, 0, 0])

const scaleSteps = [0, 3.5, 7, 14, 20]
let guidance_scale = 7

// The `onChange` function is a callback function that is called when the value of the input changes.
// It takes an `input` parameter and assigns its value to the `text` ref variable. It also logs the
// value of `text` and the value at index 2 of the `swButtons` ref array to the console.
let onChange = (input) => {
  text.value = input
  console.log(text.value)
  console.log(swButtons.value[2])
}

// The `onKeyPress` function is a callback function that is called when a key is pressed on the
// keyboard. It takes a `button` parameter, which represents the key that was pressed, and logs the
// value of `button` to the console.
let onKeyPress = (button: string) => {
  console.log('button', button)
}

// The `onInputChange` function is a callback function that is called when the value of the input field
// changes. It takes an `input` parameter, which represents the event object of the input change event.
let onInputChange = (input) => {
  text.value = input.target.value
  console.log(text.value)
}

// The `buttonswap` function is a callback function that is called when a switch button is clicked. It
// takes a `pos` parameter, which represents the position of the switch button that was clicked.
let buttonswap = (pos: Number) => {
  for (let i = 0; i < 5; i++) {
    swButtons.value[i] = 0
  }
  swButtons.value[pos] = 1
  guidance_scale = scaleSteps[pos]
}

let next = () => {
  let data:Object = {
      "prompt": text.value,
      "guidance_scale": guidance_scale
  }
 
  console.log(imgStore.scribble)
  imgStore.promptdata = Object.create(data)
  console.log(imgStore.promptdata)
  if(imgStore.scribble !== undefined){
      route.push('result')
  } else {
    route.push('start')
  }
  
}
</script>

<template>
  <div id="background">
    <div id="content">
      <div id="header">
        <div>
          
        </div>
        <h2>Was hast du gemalt?</h2>
      </div>

      <div id="menu">
        <div id="settings">
          <div>
            <h3>Genauigkeit</h3>
            <p>Wie sehr soll sich die KI an deine Zeichnung halten?</p>
            <div id="switch">
              <div class="swwrp">
                <div class="swbtn" :class="{ active: swButtons[0] }" @click="buttonswap(0)"></div>
                <p>ungenau</p>
              </div>
              <div class="swbtn" :class="{ active: swButtons[1] }" @click="buttonswap(1)"></div>
              <div class="swwrp">
                <div class="swbtn" :class="{ active: swButtons[2] }" @click="buttonswap(2)"></div>
                <p>Standart</p>
              </div>
              <div class="swbtn" :class="{ active: swButtons[3] }" @click="buttonswap(3)"></div>
              <div class="swwrp">
                <div class="swbtn" :class="{ active: swButtons[4] }" @click="buttonswap(4)"></div>
                <p>genau</p>
              </div>
            </div>
          </div>

          <textarea
            v-model="text"
            placeholder="Gib in diesem Feld an, was du gemalt hast. 
Du kannst zusätzlich angeben, ob es z.B. in 3D dargestellt werden soll
oder im Stil deiner Lieblingskünstler*in."
            id="text"
          ></textarea>
        </div>

        <img :src="imgStore.scribble" alt="" width="552px" height="333px" id="scribble" />
      </div>

      <div id="buttn" @click="next"><h3>Bild erstellen</h3></div>

      <SimpleKeyboard @onChange="onChange" @onKeyPress="onKeyPress" :input="input"></SimpleKeyboard>
    </div>
  </div>
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
  display: flex;
  align-items: center;
  justify-content: center;
}

.swbtn {
  width: 102px;
  height: 40px;
  background-color: #d9d9d9;
  border-radius: 6px;
}

.active {
  border: 3px solid var(--black, #161617);
  background: #8bb174;
}

.swwrp {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#switch {
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-top: 20px;
}

#scribble {
  width: 552px;
  height: 333px;
  border-radius: 22px;
  border: 4px solid #000;
  background: #fff;
  /* Schatten 1 */
  box-shadow: 2px 4px 0px 0px #161617;
}

#menu {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
}

#content {
  display: flex;
  flex-direction: column;
  width: 80vw;
  gap: 20px;
}

#settings {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 20px;
}

#text {
  outline: none;
  resize: none;
  height: 150px;
  text-align: left;
  color: var(--black, #161617);
  font-family: Futura PT;
  font-size: 1.2rem;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  padding: 10px;
  border-radius: 17px;
  border: 4px solid var(--black, #161617);
  box-shadow: 2px 4px 0px 0px #161617;
}

#buttn {
  width: 279px;
  height: 74px;
  flex-shrink: 0;
  border-radius: 14px;
  border: 4px solid var(--black, #161617);
  background: #8bb174;
  /* Schatten 1 */
  box-shadow: 2px 4px 0px 0px #161617;
  display: flex;
  align-items: center;
  justify-content: center;
}

#buttn:active {
  box-shadow: 0px 0px 0px 0px #161617;
}
</style>
