/**
 * Created by yangzhiqiang on 2018/4/9.
 */
import request from 'superagent'
const state = {
  isRegister: false,
  isLogin: false,
  username: ''
}
const mutations = {
  register_user (state, {userInfo}){
    console.log(userInfo)
    request
      .post('/api/register')
      .send({
        nicknameValue: userInfo.nickname,
        passwordValue: userInfo.password,
      })
      .end((err, res) => {
        if (!err) {
          console.log(res)
          if (res.body.result == "success") {
            state.isRegister = true
            console.log("success")
            console.log(state.isRegister)
          }
        }
      })
  },
  login_user (state, {userInfo}){
    console.log(userInfo)
    state.isLogin = userInfo.isLogin
    state.username = userInfo.username
    // request
    //   .post('/api/login')
    //   .send({
    //     nicknameValue: userInfo.nickname,
    //     passwordValue: userInfo.password,
    //   })
    //   .end((err, res) => {
    //     if (!err) {
    //       console.log(res)
    //       if(res.body.result == "success"){
    //         state.isLogin = true
    //         state.username = res.body.username
    //         console.log("success")
    //         console.log(state.isLogin)
    //       }else{
    //         alert("登录失败")
    //       }
    //     }
    //   })
  },
  logout_user (state){
    request
      .post('/api/logout')
      .end((err, res) => {
        if (!err) {
          console.log(res)
          if (res.body.result == "success") {
            state.isLogin = false
            state.username = null
            console.log("success")
            console.log(state.isLogin)
          } else {
            alert("登出失败")
          }
        }
      })
  }
}
const actions = {
  register_user: ({commit}, userInfo) => commit('register_user', {userInfo}),
  login_user: ({commit}, userInfo) => commit('login_user', {userInfo}),
  logout_user: ({commit}) => commit('logout_user'),
}
const getters = {
  isRegister: state => {
    return state.isRegister
  },
  isLogin: state => {
    return state.isLogin
  },
  username: state => {
    return state.username
  },
}
export default {
  state,
  getters,
  actions,
  mutations
}
