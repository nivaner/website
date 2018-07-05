/**
 * Created by yangzhiqiang on 2018/4/7.
 */

import * as types from '../mutation-types'

export const resetUser = ({ commit }) => {
  commit(types.UPDATE_VIEWING_USER, {})
}
