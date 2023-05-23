<template>
    <twfy-component/>
</template>

<script>
import TwfyComponent from "@/components/TwfyComponent.vue"

    export default{
        name:'twfy-app',
        data(){
            return {
                app:{},
            }
        },

        components:{
            TwfyComponent
        }
    }
</script>