<template>
    <div class = "container">
        <h1>Dgr Page</h1>
        <div class="container options">
            <button @click="toCreate" type="button" class="btn btn-primary">Create</button>
        </div>
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

        methods:{
            toCreate(){
                this.$router.push({name:'dgr_create'})
            }
        },

        components:{
            DgrData
        }
    }
</script>