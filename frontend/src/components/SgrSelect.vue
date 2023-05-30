<template>
    <div class="container">
        <h6>Выберите StuGroup:</h6>
        <v-select v-model="cur_sgr" :options="stg_list" label="name"/>
    </div>
</template>


<script>
import { StuGroup } from '@/api/api';

export default{
    name:'sgr-select',

    data(){
        return {
            stg_list:[],

            cur_sgr:{
                type: Object,
                default:''
            }
        }
    },

    methods:{
        async getSgr(){
            let data = await StuGroup.objects.filter()
            this.stg_list = data
        },

        async _cheak(name){
            let params = {
                name__icontains: name
            }
            let data = await StuGroup.objects.filter(params)
            if (data.length === 1){
                return true
            }
            return false
        },

        selectSgr(sgr_id){
            this.$emit('setSgr', sgr_id)
        },

        setNull(){
            this.$emit('defaultSgr')
        }
    },

    watch:{
        cur_sgr(newValue){
            if (newValue != null){
                if (this._cheak(newValue.name)){
                    this.selectSgr(newValue.sgr_id)
                }
            }else{
                this.setNull()
            }
        }
    },

    mounted(){
        this.getSgr()
    },

    components: {
        vSelect: window["vue-select"]
    },
}
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>