<template>
    <div class = "container">
        <form>
            <h1>Create Dgr Page</h1>
            <typ-select @setTyp="setTyp" @defaultTyp="defaultTyp"/>
            <br/>
            <sgr-select @setSgr="setSgr" @defaultSgr="defaultSgr"/>
            <br/>
            <version-select @setVer="setVer" @defaultVer="defaultVer"/>
            <br/>
            <tpr-select @setTpr="setTpr" @defaultTpr="defaultTpr"/>
            <br/>
            <divdgr-select @setDiv="setDiv" @defaultDiv="defaultDiv"/>
            <br/>
            <button @click="saveDgr" type="button" class="btn btn-primary">Create</button>
        </form>
    </div>
</template>

<script>
import { DgrPeriod } from '@/api/api';
import TypSelect from '@/components/TypSelect.vue';
import SgrSelect from '@/components/SgrSelect.vue';
import VersionSelect from '@/components/VersionSelect.vue';
import TprSelect from '@/components/TprSelect.vue';
import DivdgrSelect from '@/components/DivdgrSelect.vue';

export default{
    name:'dgr-create',
    data(){
        return {
            dgr:{}          
        }
    },

    methods:{
        setTyp(typ_id){
            this.dgr.typ_typ = typ_id
        },

        defaultTyp(){
            this.dgr.typ_typ = null 
        },

        setSgr(sgr_id){
            this.dgr.sgr_sgr = sgr_id
        },

        defaultSgr(){
            this.dgr.sgr_sgr = null
        },

        setVer(ver_id){
            this.dgr.ver_ver = ver_id
        },

        defaultVer(){
            this.dgr.ver_ver = null
        },

        setTpr(tch_id){
            this.dgr.tch_tch = tch_id
        },

        defaultTpr(){
            this.dgr.tch_tch = null
        },

        setDiv(div_id){
            this.dgr.div_div = div_id
        }, 

        defaultDiv(){
            this.dgr.div_div = null
        },

        async saveDgr(){
            if(this._check_value()){
                console.log('true')
                await DgrPeriod.objects.save(this.dgr, null)
            }
            console.log('false')
        },

        _check_value(){
            console.log('obj', this.dgr)
            for (let prop in this.dgr) {
                if (this.dgr[prop] === null) {
                    return false
                }
            }
            return true
        }
    },
    
    components:{
        TypSelect,
        SgrSelect,
        VersionSelect,
        TprSelect,
        DivdgrSelect
    }

}
</script>