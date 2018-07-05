/**
 * Created by yangzhiqiang on 2018/4/7.
 */

import request from 'superagent'

const state = {
  question_no: 0,
  // ctrl: true
}

const mutations = {
  create_title (state, {questionnaireInfo},self){
    console.log(questionnaireInfo)
    request
      .post('/api/createQuestionnaire')
      .send({
        title: questionnaireInfo.title,
        subtitle: questionnaireInfo.subtitle,
      })
      .end((err, res) => {
        if (!err) {
          console.log(res)
          if(res.body.result == "success"){
            state.question_no ++;
            console.log("success")
            // wj_id = res.body.wj_id
            // questionnaireInfo.self.$router.push('/createQuestionnaire/preview');
            questionnaireInfo.self.$router.push({name: 'preview', params: {id: res.body.wj_id}})
          }
          else if(res.body.result == "noLogin"){
            console.log("未登录")
            alert("未登录，请先登录！")
          }
        }
      })
  },
  create_question (state, {questionInfo},self){
    console.log(questionInfo)
    request
      .post('/api/createQuestion')
      .send({
        q_title: questionInfo.q_title,
        options: questionInfo.options,
        option_type: questionInfo.option_type,
        wj_id: questionInfo.wj_id
      })
      .end((err, res) => {
        if (!err) {
          console.log(res)
          if(res.body.result == "success"){
            state.question_no ++;
            console.log("success")
            questionInfo.self.$router.push({name: 'preview', params: {id: res.body.wj_id}})

          }
          else if(res.body.result == "noLogin"){
            console.log("未登录")
            alert("未登录，请先登录！")
          }
        }
      })

  },
}

const actions = {
  create_title: ({commit}, questionnaireInfo) => commit('create_title', {questionnaireInfo}),
  create_question: ({commit}, questionInfo) => commit('create_question', {questionInfo}),

}

const getters = {
  question_no: state => {
    return state.question_no
  },
  ctrl: state => {
    return state.question_no
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
