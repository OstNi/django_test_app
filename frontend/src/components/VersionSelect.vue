<template>
     <div class="container">
        <h6>Выберите Version:</h6>
        <v-select v-model="cur_ver" :options="ver_list" label="info"/>
    </div>
</template>

<script>
import { Version } from '@/api/api';

export default{
    name:'ver-select',

    data(){
        return {
            ver_list:[],

            cur_ver:{
                type: Object,
                default:''
            }
        }
    },

    methods:{
        async getVer(){
            let data = await Version.objects.filter()
            this.ver_list = data
        },

        async _cheak(info){
            let params = {
                info__icontains: info
            }
            let data = await Version.objects.filter(params)
            if (data.length === 1){
                return true
            }
            return false
        },

        selectVer(ver_id){
            this.$emit('setVer', ver_id)
        },

        setNull(){
            this.$emit('defaultVer')
        }
    },

    watch:{
        cur_ver(newValue){
            if (newValue != null){
                if (this._cheak(newValue.info)){
                    this.selectVer(newValue.ver_id)
                }
            }else{
                this.setNull()
            }
        }
    },

    mounted(){
        this.getVer()
    },

    components: {
        vSelect: window["vue-select"]
    },
}
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>