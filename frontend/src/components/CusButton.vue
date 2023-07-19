<script setup lang="ts">
const props = defineProps(['text'])
</script>

<template>
  <div id="buttonwrapper">
    <p>{{ props.text }}</p>
  </div>
</template>

<style scoped>
#buttonwrapper {
  padding: 10px 10px 15px 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 140px;
  background-color: var(--orange);
  border-radius: 0.8125rem;
  border: 2px solid var(--black, #161617);
  background: var(--yellow, #ffc62a);
  box-shadow: 2px 4px 0px 0px #161617;
}

#buttonwrapper:active {
  box-shadow: 2px 4px 0px 0px rgba(22, 22, 23, 0);
}
</style>
