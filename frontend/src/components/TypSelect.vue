<template>
    <div class="container">
        <h6>Выберите TyPeriod:</h6>
        <v-select v-model="curr_typ_id" :options="typ_list" label="typ_id"/>
    </div>
</template>

<script>
import { TyPeriod } from '@/api/api';

export default{
    name:'typ-select',
    emits:['cur_typ'],

    data(){
        return {
            typ_list:[],
            curr_typ_id:''
        }
    },

    methods:{
        async getTyp(){
            let data = await TyPeriod.objects.filter()
            this.typ_list = data
        },

        async _cheak(typ_id){
            let params = {
                typ_id__icontains: typ_id
            }

            let data = await TyPeriod.objects.filter(params)
            if (data.length === 1){
                return true
            }

            return false
        },

        selectTyp(typ_id){
            this.$emit('setTyp', typ_id)
        },

        setNull(){
            this.$emit('defaultTyp')
        }
        
    },

    watch:{
        curr_typ_id(newValue){
            if (newValue != null){
                if (this._cheak(newValue.typ_id)){
                    this.selectTyp(newValue.typ_id)
                }
            }
            else{
                this.setNull()
            }
        }
},

    mounted(){
        this.getTyp()
    },

    components: {
        vSelect: window["vue-select"]
    },
}
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>