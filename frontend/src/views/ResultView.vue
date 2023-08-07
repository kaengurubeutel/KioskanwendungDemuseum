<script setup lang="ts">
    import LoadingAnim from '@/components/LoadingAnim.vue';
</script>

<template>
    <div id="wrapper">
        <LoadingAnim></LoadingAnim>
    </div>
</template>

<style scoped>

    #wrapper{
        height: 100vh;
        width: 100vw;
        background: #FF8A1E;
        position: absolute;
        left: 0;
        top: 0;
        z-index: 5;
    }


</style>