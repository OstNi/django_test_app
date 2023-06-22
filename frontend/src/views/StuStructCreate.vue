<template>
    <div class = "container">
        <form>
            <h1>Create StuStruct</h1>
            <br/>
            <div class="container">
                <h6>Выберите StuGroup:</h6>
                <input v-model="dgr.sgr_sgr.name" class="form-control" placeholder="Enter name of group"/>
                <p>{{dgr.sgr_sgr.name?dgr.sgr_sgr.name:'-'}}</p>
            </div>
            <br/>
            <typ-select @setTyp="setTyp" @defaultTyp="defaultTyp"/>
            <!-- <br/>
            <sgr-select @setSgr="setSgr" @defaultSgr="defaultSgr"/> -->
            <br/>
            <version-select @setVer="setVer" @defaultVer="defaultVer"/>
            <br/>
            <tpr-select @setTpr="setTpr" @defaultTpr="defaultTpr"/>
            <br/>
            <divdgr-select @setDiv="setDiv" @defaultDiv="defaultDiv"/>
            <br/>
            <button @click="saveDgr" type="button" class="btn btn-primary">Create</button>
        </form>
        <br/>
    </div>
</template>

<script>
import { DgrPeriod } from '@/api/api';
import TypSelect from '@/components/TypSelect.vue';
//import SgrSelect from '@/components/SgrSelect.vue';
import VersionSelect from '@/components/VersionSelect.vue';
import TprSelect from '@/components/TprSelect.vue';
import DivdgrSelect from '@/components/DivdgrSelect.vue';

export default{
    name:'stu-create',
    data(){
        return {
            dgr:{
                sgr_sgr:{}
            },
            response:{}          
        }
    },

    methods:{
        setTyp(typ){
            this.dgr.typ_typ = typ.typ_id
        },

        defaultTyp(){
            this.dgr.typ_typ = null 
        },

        // setSgr(stu){
        //     this.dgr.sgr_sgr = stu.sgr_id
        // },

        // defaultSgr(){
        //     this.dgr.sgr_sgr = null
        // },

        setVer(ver){
            this.dgr.ver_ver = ver.ver_id
        },

        defaultVer(){
            this.dgr.ver_ver = null
        },

        setTpr(tpr){
            this.dgr.tch_tch = tpr.tch_id
        },

        defaultTpr(){
            this.dgr.tch_tch_id = null
        },

        setDiv(div){
            this.dgr.div_div = div.div_id
        }, 

        defaultDiv(){
            this.dgr.div_div = null
        },

        async saveDgr(){
            if(this._check_value()){
                console.log('true')
                this.response = await DgrPeriod.objects.save(this.dgr, null)
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
        VersionSelect,
        TprSelect,
        DivdgrSelect
    }

}
</script>