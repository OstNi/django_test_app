<template>
    <div class="container">
       <h6>Выберите TprChapter:</h6>
       <v-select v-model="cur_tpr" :options="tpr_list" label="name"/>
   </div>
</template>

<script>
import { TprChapter } from '@/api/api';

export default{
   name:'tpr-select',

   data(){
       return {
           tpr_list:[],

           cur_tpr:{
               type: Object,
               default:''
           }
       }
   },

   methods:{
        async getTpr(){
            this.tpr_list = await TprChapter.objects.filter()
        },

        async _cheak(name){
            let params = {
                name__icontains: name
            }
            let data = await TprChapter.objects.filter(params)
            if (data.length === 1){
                return true
            }
            return false
        },

        selectTch(tch_id){
            this.$emit('setTpr', tch_id)
        },

        setNull(){
            this.$emit('setTpr')
        }
   },

    watch:{
        cur_tpr(newValue){
            if (newValue != null){
                if (this._cheak(newValue.name)){
                    this.selectTch(newValue.tch_id)
                }
            }else{
                this.setNull()
            }
        }
    },

   mounted(){
       this.getTpr()
   },

   components: {
       vSelect: window["vue-select"]
   },
}
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>