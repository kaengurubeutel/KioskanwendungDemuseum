<script setup lang="ts">
    import { ref, onMounted} from 'vue';
    const loadingtime = ref(30)
    const timer = (ms) => new Promise((res) => setTimeout(res, ms))
    let bgn = ref(null)
    let lense = ref(null)
    let mouseX = ref(0)
    let mouseY = ref(0)

    let mousemove = (e) => {
        mouseX.value = (e.clientX + document.body.scrollLeft);
        mouseY.value = (e.clientY + document.body.scrollTop);
        bgn.value.style.clipPath = 'circle(200px at ' + (mouseX.value- 200) + 'px ' + (mouseY.value-98) + 'px)';
        lense.value.style.top = mouseY.value - 200  + 'px';
        lense.value.style.left = mouseX.value - 200 + 'px';
    }


    import { useRouter } from 'vue-router'

    const route = useRouter()


    let loading = async (time:number) => {
         for (let i = time; i > -1; i--) {
        if (i===0)  route.push("start");
        loadingtime.value = i;
        await timer(1000)
    }
    }

    onMounted(()=>{
        loading(30);
    });
</script>

<template>
    
    <div @mousemove="mousemove" >
        
        <div>
            <div id="resultimage" ></div>
            <img src="../assets/Background2.png" alt="" id="bckgrnd2" ref="bgn" />
            <div id="lense" ref="lense">
              <div id="handle"></div>
            </div>
        </div>
        
        

        <div id="loadwrapp">
            <p>{{loadingtime}}</p>
            <svg id="loading" xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 33 33" fill="none">
            <path d="M31.1837 15.8579C32.1789 15.8145 33.0312 16.588 32.9658 17.582C32.7456 20.9304 31.5078 24.1482 29.3965 26.793C26.9083 29.9098 23.3755 32.02 19.4516 32.7331C15.5277 33.4461 11.4783 32.7139 8.05264 30.6718C4.62697 28.6297 2.05687 25.4159 0.817852 21.6251C-0.421165 17.8342 -0.24524 13.7229 1.31308 10.0518C2.87139 6.3807 5.70663 3.39823 9.29423 1.65621C12.8818 -0.0858096 16.979 -0.469473 20.8276 0.576204C24.0934 1.46352 26.9927 3.32906 29.1479 5.90105C29.7878 6.66458 29.5568 7.79217 28.7281 8.34488V8.34488C27.8993 8.8976 26.788 8.66335 26.1251 7.91975C24.4709 6.06406 22.3055 4.71596 19.8817 4.05744C16.8745 3.24038 13.6732 3.54016 10.8699 4.90132C8.06671 6.26248 5.85135 8.59288 4.63373 11.4614C3.41612 14.3299 3.27865 17.5423 4.24678 20.5043C5.21491 23.4664 7.2231 25.9775 9.89981 27.5731C12.5765 29.1688 15.7406 29.7409 18.8066 29.1838C21.8726 28.6266 24.633 26.9778 26.5772 24.5424C28.1441 22.5795 29.0953 20.2128 29.3343 17.7383C29.43 16.7467 30.1885 15.9014 31.1837 15.8579V15.8579Z" fill="#161617"/>
            </svg>
        </div>
        
    </div>

</template>

<style scoped>
    p {
        text-align: center;
        position: relative;
        left:0px;
        top: 40px;
    }

    #loading{
        animation: rotate 2s cubic-bezier(0.39, 0.575, 0.565, 1) infinite;
    }

    @keyframes rotate {
        0% {
            transform: rotate(0deg);
        }
        100%{
            transform: rotate(359deg);
        }
    }

    #resultimage{
        position: relative;
        width: 1500px;
        height: 800px;
        background-color: aliceblue;
        border-radius: 40px;
    }

    #loadwrapp {
        position: absolute;
        width: 50px;
        bottom: 110px;
        right: 230px;
    }

    #bckgrnd2 {
        position: absolute;
        top: 98px;
        width: 1500px;
        height: 800px;
        background-color: aliceblue;
        border-radius: 40px;
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