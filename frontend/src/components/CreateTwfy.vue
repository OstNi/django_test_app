<template>
    <div class="container">
        <div class = "application col-8">
            <h2> Создать TwForYear </h2>
            <div class = 'col-8'>

                <div class = "app-field">
                    <div> TY_ID </div>
                    <input v-model="twfy.ty_ty" class="form-control app-form" placeholder="2022"/>
                </div>

                <div class = "app-field">
                    <div> WOT_ID</div>
                    <input v-model="twfy.wt_wot" class="form-control app-form" placeholder="1"/>
                </div>
                <br/>
                <button class="btn btn-primary send-btn" @click="save">Создатть</button>
            </div>
        </div>
    </div>
</template>

<script>
import {TwForYear} from "@/api/api"

    export default{
        name:'createtwfy-form',
        data(){
            return {
                twfy:{}
            }
        },
       
        methods:{
            async save(){
                let twfy = this.twfy     
                await TwForYear.objects.save(twfy)
                this.$router.push('/twfy/')
            }
        }
    }
</script>