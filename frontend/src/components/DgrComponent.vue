<template>
  <h1>DgrPeriod page</h1>
  <div class = "container">
    <table class = "table table-striped-columns">
      <tr>
        <th scope="col">ID</th>
        <th scope="col">TPD_ID</th>
        <th scope="col">VER_ID</th>
        <th scope="col">SGR_ID</th>
        <th scope="col">TYP_ID</th>
        <th scope="col">DIV_ID</th>
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