<script setup lang="ts">

import { ref } from 'vue';
const loadingtextArray = ["Buntstifte sortieren", "Kurze Kreativpause", "Pinsel aussuchen", "Radierkrümel wegwischen"]
const loadingtext = ref(loadingtextArray[0])



</script>

<template>
    <div id="wrp">
            <div class="dotwrp">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
            <h3> {{loadingtext}}</h3>
    </div>
</template>

<style scoped>

.dotwrp {
    display: flex;
    flex-direction: row;
    gap: 10px;
}

.dot {
    border-radius: 50%;
    width: 10px;
    height: 10px;
    background: #161617;
}

#wrp {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 80px;
    margin: 100px;
}

</style>