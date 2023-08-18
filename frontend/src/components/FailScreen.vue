<script setup lang="ts"></script>

<template>
  <div>
    <div id="text">
      <h1>Ups ...</h1>
      <h2>da ist wohl was <br />schief gegangen</h2>
      <div id="backbutton" @click="$router.push('/start')"><h3>Neu starten</h3></div>
    </div>

    <img src="../assets/catasset.png" alt="" />
  </div>
</template>

<style scoped>
#text {
  position: absolute;
  display: flex;
  flex-direction: column;
  gap: 20px;
  left: 550px;
  top: 240px;
}

#backbutton {
  background-color: #8bb174;
  border-radius: 13px;
  border: 2px solid var(--black, #161617);
  text-align: center;
  width: 170px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 2px 4px 0px 0px #161617;
}

#backbutton:active {
  box-shadow: 0px 0px 0px 0px #161617;
}
</style>
