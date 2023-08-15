<script setup lang="ts">
import { onMounted, ref } from "vue";


    const loadingtextArray = ["Buntstifte sortieren", "Kurze Kreativpause", "Pinsel aussuchen", "Radierkrümel wegwischen"]
    const timer = ms => new Promise(res => setTimeout(res, ms))
    const text = ref("")

   // The `load()` function is an asynchronous function that is responsible for updating the `text`
   // variable with different values from the `loadingtextArray` array every 3 seconds.
    async function load() {
        for(let i = 0; i<100 ; i++){
            console.log(i)
            text.value = loadingtextArray[i%4]
            await timer(3000);
        }
    }

onMounted(()=>{
    load();
})
</script>

<template>
    <div id="wrp">
            <div class="dotwrp">
                <div class="dot dot1"></div>
                <div class="dot dot2"></div>
                <div class="dot dot3"></div>
            </div>
           <h3>{{text}}</h3>
            

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
    animation: loading 1s cubic-bezier(0.39, 0.575, 0.565, 1)  infinite;
}

@keyframes loading {
    0%,
  100% {
    transform: scale(1);
   
  }
  42% {
    
  }
  50% {
    transform: scale(1.5);
    
  }
}

.dot.dot1 {
    animation-delay: 0.2s;
}


.dot.dot2 {
    animation-delay: 0.4s;
}

.dot.dot3 {
    animation-delay: 0.6s;
}


#wrp {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 80px;
    margin: 100px;
}

h3 {
    text-align: center;
}


</style>