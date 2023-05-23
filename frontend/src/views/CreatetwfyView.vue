<template>
    <create-twfy/>
</template>

<script>
import CreateTwfy from "@/components/CreateTwfy.vue"

    export default{
        name:'createtwfy-app',
        data(){
            return {
                app:{},
            }
        },

        components:{
            CreateTwfy
        }
    }
</script>