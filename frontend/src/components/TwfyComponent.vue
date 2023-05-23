<template>
    <h1>TwForYears page</h1>
    <div class = "container">
      <table class = "table table-striped-columns">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">TY_TY</th>
          <th scope="col">WOT_ID</th>
        </tr>
        <tr v-for="(twfy, idx) in tw_for_year_list" :key="twfy.twfy_id">
          <td>{{twfy.twfy_id}}</td>
          <td>{{twfy.ty_ty}}</td>
          <td>{{twfy.wt_wot}}</td>
          <td><button @click="deleteTwfy(twfy, twfy.twfy_id, idx)" class = "btn-danger">удалить</button></td>
        </tr>
      </table>
    </div>
  </template>
  
  
  <script>
  import {TwForYear} from '@/api/api'
  
  export default(await import('vue')).defineComponent({
    name: "twfy-component",
  
    data(){
      return{
        tw_for_year_list:[]
      }
    },
  
    methods:{
      async getTwfy(){
        let data = await TwForYear.objects.filter()
        this.tw_for_year_list = data
      },

      async deleteTwfy(twfy, twfy_id, idx){
        await TwForYear.objects.delete(twfy, twfy_id)
        //console.log(twfy)
        this.tw_for_year_list.splice(idx,1)
      }
    },
  
    mounted(){
      this.getTwfy()
    }
  })
  </script>