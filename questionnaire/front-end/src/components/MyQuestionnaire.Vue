<template>
  <div class="myQuestionnaire">
    <el-row class="cards">
      <div v-for="wj in wjs">
        <el-col :span="8">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>{{wj.title}}</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="read(wj.id)">查看问卷</el-button>
            </div>
            <div class="text item">
              <div class="wj-id">问卷固定id：{{wj.id}}</div>
            </div>

            <div v-if="wj.complete">
              <div class="text item" v-if="!wj.release_date">
                <el-button type="primary" @click="publish(wj.id)">发布问卷</el-button>
              </div>
              <div v-else>
                <div class="text item">
                  问卷发布时间：
                  <div class="wj-release-date">{{wj.release_date}}</div>
                </div>
                <div v-if="!wj.collect_date">
                  <div class="text item">
                    问卷填写链接：
                    <router-link :to="'/answer/'+wj.id"> http://localhost:8080/#/answer/{{wj.id}}</router-link>
                  </div>
                  <div class="text item">
                    <el-button type="primary" @click="analysis(wj.id)">查看回收概况</el-button>
                    <el-button type="primary" @click="stop(wj.id)">暂停回收</el-button>
                  </div>
                </div>
                <div v-else>
                  <div class="text item">
                    回收时间：
                    <div class="wj-collect-date">4{{wj.collect_date}}</div>
                  </div>
                  <div class="text item">
                    <el-button  type="success" @click="analysis(wj.id)">查看完整回收概况</el-button>
                  </div>
                </div>
              </div>

            </div>
            <div v-else>
              <div class="text item">
                <el-button type="primary" @click="read(wj.id)">继续创建</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </div>
    </el-row>
  </div>
</template>

<script type="text/ecmascript-6">
  import request from 'superagent'
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    data () {
      return {
        wjs: {},
      }
    },
    created () {
      // 组件创建完后获取数据，
      // 此时 data 已经被 observed 了
      this.fetchData()
    },
    watch: {
      // 如果路由有变化，会再次执行该方法
      '$route': 'fetchData'
    },
    methods: {
      fetchData () {
        this.error = this.post = null
        this.loading = true
        request
          .post('/api/myQuestionnaire')
          .end((err, res) => {
            this.loading = false
            if (!err) {
              if (res.body.result == "success") {
                this.wjs = res.body.wjs,
                  console.log(this.wjs, "wjswjs")
              }
            }
          })
      },
      read(id){
        this.$router.push({name: 'preview', params: {id: id}})
      },
      publish (id) {
        request
          .post('/api/publish')
          .send({
            wj_id: id,
          })
          .end((err, res) => {
            if (!err) {
              console.log(res)
              if (res.body.result == "success") {
                alert("问卷已发布")
                this.fetchData();
              } else {
                alert("发布失败")
              }
            }
          })
      },
      stop (id) {
        request
          .post('/api/stop')
          .send({
            wj_id: id,
          })
          .end((err, res) => {
            if (!err) {
              console.log(res)
              if (res.body.result == "success") {
                alert("问卷已停止回收")
                this.fetchData();
              } else {
                alert("回收失败")
              }
            }
          })
      },
      analysis (id) {
        this.$router.push({name: 'Analysis', params: {id: id}})
      }
    },
    filters: {
      jsonData: function (value) {
        if (!value) return ''
        console.log(value)
        console.log(JSON.parse(value))
        return JSON.parse(value)
      },
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
    }
  }
</script>

<style lang="scss" rel="stylesheet/scss">

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 380px;
    height: 301px;
    margin: 40px auto 0;
  }

</style>
