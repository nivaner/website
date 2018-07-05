/**
 * Created by yangzhiqiang on 2018/4/7.
 */
import Vue from 'vue'
import Vuex from 'vuex'

import user from './moudules/user'
import result from './moudules/result'
import questionnaire from './moudules/questionnaire'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user,
    result,
    questionnaire
  }
})
