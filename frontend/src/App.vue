<script setup lang="ts">
import { RouterView, RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue'
const route = useRouter()
onMounted(() => {
  route.push('/start')
})
</script>

<template>
  <RouterView></RouterView>
</template>

<style scoped></style>
