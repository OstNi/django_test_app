<template>
    <dgr-component/>
</template>

<script>
import DgrComponent from "@/components/DgrComponent.vue"

    export default{
        name:'dgr-app',
        data(){
            return {
                app:{},
            }
        },

        components:{
            DgrComponent
        }
    }
</script>