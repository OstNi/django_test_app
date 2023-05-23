<template>
    <twblock-component/>
</template>

<script>
import TwblockComponent from "@/components/TwblockComponent.vue"

    export default{
        name:'twblock-app',
        data(){
            return {
                app:{},
            }
        },

        components:{
            TwblockComponent
        }
    }
</script>