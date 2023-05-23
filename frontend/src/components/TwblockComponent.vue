<template>
    <div class = "dgr">
      <div class = "dgr-container">
        <table class = "dgr-data">
          <tr>
            <th>TWB_ID</th>
            <th>VAL</th>
            <th>CONV_VAL</th>
            <th>WOT_ID</th>
            <th>DGR_ID</th>
            <th>INITIALIZED_BY WOT_ID</th>
          </tr>
          <tr v-for="twb in tw_blok_list" :key="twb.twb_id">
            <td>{{twb.twb_id}}</td>
            <td>{{twb.val}}</td>
            <td>{{twb.conv_value}}</td>
            <td>{{twb.wt_wot}}</td>
            <td>{{twb.dgp_dgp}}</td>
            <td>{{twb.wt_wot_id_initialized_by}}</td>
          </tr>
        </table>
      </div>
    </div>
  </template>
  
  
  <script>
  import {TwBlock} from '@/api/api'
  
  export default(await import('vue')).defineComponent({
    name: "twblock-component",
  
    data(){
      return{
        tw_blok_list:[]
      }
    },
  
    methods:{
      async getTwBlock(){
        let data = await TwBlock.objects.filter()
        this.tw_blok_list = data
      }
    },
  
    mounted(){
      this.getTwBlock()
    }
  })
  </script>