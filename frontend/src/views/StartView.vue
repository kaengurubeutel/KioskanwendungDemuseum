<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
import CusButton from '@/components/CusButton.vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
import background from '../assets/Background2.png'
const canvas = ref(null)
let bgn = ref(null)
let lense = ref(null)
let mouseX = ref(0)
let mouseY = ref(0)

let mousemove = (e) => {
  mouseX.value = (e.clientX + document.body.scrollLeft);
  mouseY.value = (e.clientY + document.body.scrollTop);
  bgn.value.style.clipPath = 'circle(200px at ' + mouseX.value + 'px ' + mouseY.value + 'px)';
  lense.value.style.top = mouseY.value - 200 + 'px';
  lense.value.style.left = mouseX.value - 200 + 'px';
}

</script>

<template>
  <main @mousemove="mousemove">
    <div id="mainpad" >
      <div id="wr">
        <h1>
          KI: <br />
          Zeichen <br />
          Zauber
        </h1>
        <h3>
          Erweitere deine Kreativität! <br />
          Zeichne mit deinem Finger,<br />
          schreibe, wie es aussehen soll<br />
          und die KI “zaubert” ein Bild heraus.
        </h3>
        <CusButton
          text="Zeichnen"
          @click="
            $router.push('draw')
          "
        ></CusButton>
      </div>
    </div>

    <img src="../assets/Background2.png" alt="" id="bckgrnd2" ref="bgn" />
    <div id="lense" ref="lense">
      <div id="handle"></div>
    </div>
    <img src="../assets/Background1.png" alt="backgrnd" id="bckgrnd1" />
  </main>
</template>

<style scoped>

main{
  position: absolute;
  width: 100vw;
  height: 100vh;
  left:0;
  overflow: hidden;
  padding:0;
  margin:0;
}

#mainpad {
  position: absolute;
  top: 150px;
  left: 100px;
  z-index: 15;
  width: 30rem;
  height: 37rem;
  flex-shrink: 0;
  background-color: var(--orange);
  border-radius: 0.75rem;
  border: 4px solid var(--black, #161617);
  background: var(--orange-2, #ff8a1e);
  /* Schatten 1 */
  box-shadow: 2px 4px 0px 0px #161617;
  display: flex;
  align-items: center;
  justify-content: center;
}

#wr {
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4rem;
}

#bckgrnd1 {
  z-index: 10;
  position: absolute;
  scale: 100%;
  top: 270px;
  right: 280px;
}

#bckgrnd2 {
  z-index: 11;
  position: absolute;
  top: 0px;
  right: 0px;
  width: 100vw;
  height: 100vh;
  clip-path: circle(200px at 200px 200px);
}

#can {
  position: absolute;
  left: 0px;
  top: 0px;
  width: 100vw;
  height: 100vh;
}

#lense {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 11;
  width: 400px;
  height: 400px;
  border-radius: 200px;
  border: 12px solid var(--black, #161617);
}

#handle {
  position: relative;
  width: 40px;
  height: 400px;
  background-color: #161617;
  transform: rotate(-20deg);
  top: 363px;
  left: 300px;
}
</style>
