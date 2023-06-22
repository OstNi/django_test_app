<template>
  <div class = "container">
    <table class="table table-hover">
      <tr>
        <th scope="col">ID</th>
        <th scope="col">TPR_CHAPTER</th>
        <th scope="col">STU_GROUP</th>
        <th scope="col">TY_PERIOD</th>
        <th scope="col">DIVISION</th>
        <th scope="col">VERSION_INFO</th>
      </tr>
        <tr v-for="dgr in dgr_list" :key="dgr.dgp_id">
        <td>{{dgr.dgp_id}}</td>
        <td>{{dgr.tpr_name}}</td>
        <td>{{dgr.sgr_name}}</td>
        <td>{{dgr.typ_typ}}</td>
        <td>{{dgr.div_name}}</td>
        <td>{{dgr.ver_info}}</td>
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