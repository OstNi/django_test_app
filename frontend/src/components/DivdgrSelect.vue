<template>
    <div class="container">
       <h6>Выберите Division:</h6>
       <v-select v-model="cur_div" :options="div_list" label="name"/>
   </div>
</template>

<script>
import { Division } from '@/api/api';

export default{
   name:'div-select',

   data(){
       return {
           div_list:[],

           cur_div:{
               type: Object,
               default:''
           }
       }
   },

   methods:{
       async getDiv(){
           this.div_list = await Division.objects.filter()
       },

       async _cheak(name){
           let params = {
               name__icontains: name
           }
           let data = await Division.objects.filter(params)
           if (data.length === 1){
               return true
           }
           return false
       },

       selectDiv(div_id){
           this.$emit('setDiv', div_id)
       },

       setNull(){
        this.$emit('defaultDiv')
       }
   },

   watch:{
        cur_div(newValue){
            if (newValue != null){
                if (this._cheak(newValue.name)){
                    this.selectDiv(newValue.div_id)
                }

            }else{
                this.setNull()
            }
        }
   },


   mounted(){
       this.getDiv()
   },

   components: {
       vSelect: window["vue-select"]
   }
    
}
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>