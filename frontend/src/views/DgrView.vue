<template>
    <div class = "container">
        <h1>Dgr Page</h1>
        <dgr-data/>
    </div>
</template>

<script>
import DgrData from "@/components/DgrData.vue"

    export default{
        name:'dgr-app',
        data(){
            return {
                app:{},
            }
        },
        components:{
            DgrData
        }
    }
</script>