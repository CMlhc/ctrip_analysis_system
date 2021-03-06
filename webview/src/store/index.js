import Vue from 'vue'
import Vuex from 'vuex'
import user from './userInfo'
import usertweets from './userTweets'
import total from './tweetsTotal'
import sentiments from './sentiments'
import mutations from './mutations'
import usercomment from './userComment'
import tempid from './tempId'
import tempids from './tempids'
import group from './group'

// new
import sight from './sightInfo'
import sight1 from './sightInfo1'
import sightcomments from './sightComments'

Vue.use(Vuex)

export default new Vuex.Store({
  // 新增加的内容
  sight,
  sight1,
  sightcomments,
  // 旧的内容
  user,
  usertweets,
  tempid,
  tempids,
  group,
  usercomment,
  total,
  sentiments,
  mutations
})
