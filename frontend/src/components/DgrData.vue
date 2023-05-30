<template>
  <div class = "container">
    <table class="table table-hover">
      <tr>
        <th scope="col">ID</th>
        <th scope="col">TPR_CHAPTER</th>
        <th scope="col">STU_GROUP</th>
        <th scope="col">TY_PERIOD</th>
        <th scope="col">DIVISION</th>
        <th scope="col">VERSION_ID</th>
      </tr>
        <tr v-for="dgr in dgr_list" :key="dgr.dgp_id">
        <td>{{dgr.dgp_id}}</td>
        <td>{{dgr.tch_tch.name}}</td>
        <td>{{dgr.sgr_sgr.sgr_id}}</td>
        <td>{{dgr.typ_typ.typ_id}}</td>
        <td>{{dgr.div_div.name}}</td>
        <td>{{dgr.ver_ver.info}}</td>
      </tr>
    </table>
  </div>
</template>
  
  
<script>
import {DgrPeriod} from '@/api/api'
  
  export default(await import('vue')).defineComponent({
    name: "dgr-data",
  
    data(){
      return{
        dgr_list:[]
      }
    },
  
    methods:{
      async getDgr(){
        let data = await DgrPeriod.objects.filter()
        this.dgr_list = data
      }
    },
  
    mounted(){
      this.getDgr()
    }
  })
</script>