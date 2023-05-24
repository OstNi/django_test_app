const  DgrPeriodmUrl = '/api/dgr_periods/'
const  TimeRuleUrl = '/api/time_rules/'
const  TwBlockUrl = '/api/tw_blocks/'
const  TwForYearUrl = '/api/tw_for_years/'
const  GroupWorkUrl = '/api/group_works/'
const  DivisionUrl = '/api/divisions/'
const  TprChapterUrl = '/api/tpr_chapters/'
const  WorkTypeUrl = '/api/work_types/'
const  TyPeriodUrl = '/api/ty_periods/'
const  StuGroupUrl = '/api/stu_groups/'


import axios from "axios"


export function toURLParams(filters){
    let params = new URLSearchParams();
    for (let f in filters){
        if (Array.isArray(filters[f])){
            for (let p of filters[f]){
                if (p){
                    params.append(f,p);
                }
            }
        }else if (filters[f] && filters[f].id){
            params.append(f,filters[f]['id'])

        }else{
            if (filters[f] !=undefined){
                params.append(f,filters[f]);
            }
        }
    }
    return params
}


async function _save(url, obj, id){
    let response 
    if (id){
        response = await axios.patch(url+obj.id+'/',obj)
    }else{
        response = await axios.post(url,obj)
    }
    
    return response.data
}
  

async function _delete(url, obj, id){
    let response 
    if (obj && id){
        response = await axios.delete(url+id+'/',obj)
        console.log(response)
    }
    return response
}
   

async function _filter(url,filter){
    const response = await axios.get(url+'?'+toURLParams(filter))
    return response.data
}


async function _getById(url,id){
    const response = await axios.get(url+id+'/')
    return response.data
}
                      

function apiConstructor(apiUrl){

    let objects= {
        async save(obj, id){
            return _save(apiUrl,obj, id)
        },
        async get(obj, id){
            return _getById(apiUrl,obj, id)
        },
        async filter(filter){
            return _filter(apiUrl,filter)
        },
        async delete(obj, id){
            return _delete(apiUrl,obj, id)
        },
    }
    return {
        url:apiUrl,
        objects,
    }
}           


export let DgrPeriod = apiConstructor(DgrPeriodmUrl)
export let TimeRule = apiConstructor(TimeRuleUrl)
export let TwBlock = apiConstructor(TwBlockUrl)
export let TwForYear = apiConstructor(TwForYearUrl)
export let GroupWork = apiConstructor(GroupWorkUrl)
export let TprChapter = apiConstructor(TprChapterUrl)
export let TyPeriod = apiConstructor(TyPeriodUrl)
export let WorkType = apiConstructor(WorkTypeUrl)
export let Division = apiConstructor(DivisionUrl)
export let StuGroup = apiConstructor(StuGroupUrl)