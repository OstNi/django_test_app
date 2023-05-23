<template>
  <div class = "dgr">
    <div class = "dgr-container">
      <table class = "dgr-data">
        <tr>
          <th>DGR_ID</th>
          <th>TPD_ID</th>
          <th>VER_ID</th>
          <th>SGR_ID</th>
          <th>TYP_ID</th>
          <th>DIV_ID</th>
        </tr>
        <tr v-for="dgr in dgr_list" :key="dgr.dgp_id">
          <td>{{dgr.dgp_id}}</td>
          <td>{{dgr.tch_tch}}</td>
          <td>{{dgr.ver_ver}}</td>
          <td>{{dgr.sgr_sgr}}</td>
          <td>{{dgr.typ_typ}}</td>
          <td>{{dgr.div_div}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>


<script>
import {DgrPeriod} from '@/api/api'

export default(await import('vue')).defineComponent({
  name: "dgr-component",

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