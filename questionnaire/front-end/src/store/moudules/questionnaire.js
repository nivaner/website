/**
 * Created by yangzhiqiang on 2018/4/15.
 */
import request from 'superagent'
const state = {
  questionnaire: {},
  ques: {}
}
const mutations = {
  get_all (state){
    request
      .post('/api/preview')
      .end((err, res) => {
        if (!err) {
          if (res.body.result == "success") {
            console.log(res.body.result)
            state.questionnaire = res.body.questionnaire,
            state.ques = res.body.ques
          }
          else if(res.body.result == "noLogin"){
            console.log("未登录")
          }
        }
      })
  },
}
const actions = {
  get_all: ({commit}) => commit('get_all'),
}
const getters = {
  questionnaire: state => {
    return state.questionnaire
  },
  ques: state => {
    return state.ques
  }
}
export default {
  state,
  getters,
  actions,
  mutations
}
