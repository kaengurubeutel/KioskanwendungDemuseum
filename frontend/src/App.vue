<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
import CusButton from '@/components/CusButton.vue'
import { ref } from 'vue'

let greeting = ref('')
const update_greeting = (_greeting) => {
  greeting.value = _greeting
}
const click = () => {
  eel.get_greeting('user')(update_greeting)
  eel.hello_world()
  console.log('clicked')
}
</script>

<template>
  <main>
    <p>{{ greeting }}</p>
    <button type="button" @click="click()">Click me</button>

    <div id="mainpad">
      <div id="wr">
        <h1>Scribble Desk</h1>
        <h3>
          Erstelle deine eigenen Bilder mit <br />
          Hilfe von KI und lasse deiner <br />
          Kreativität freien Lauf.
        </h3>
        <CusButton text="starten" @click="$router.push('draw')"></CusButton>
      </div>
    </div>
  </main>
  <RouterView></RouterView>
</template>

<style scoped>
#mainpad {
  width: 37.50075rem;
  height: 47.492rem;
  flex-shrink: 0;
  background-color: var(--orange);
  border-radius: 0.75rem;
  border: 4px solid var(--black, #161617);
  background: var(--orange-2, #ff8a1e);
  /* Schatten 1 */
  box-shadow: 2px 4px 0px 0px #161617;
}

#wr {
  position: relative;
  top: 110px;
  left: 50px;
  display: inline-flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 5.5rem;
}
</style>
