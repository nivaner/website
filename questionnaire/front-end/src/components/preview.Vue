<template>
  <div class="preview">
    <el-header class="main-head">
      预览
    </el-header>
    <el-container>
      <el-header>
        <el-row>
          <div class="title">{{wj_info.title}}</div>
          <div class="subtitle">{{wj_info.subtitle}}</div>
        </el-row>
      </el-header>
      <div class="content">
        <div v-for="(que,index) in ques">
          <el-row class="mg-t">
            <el-col :span="20" :offset="2">{{index + 1}}、 {{que.q_title}}</el-col>
          </el-row>
          <el-row class="pd-l" v-if="que.q_titleType == 1">
            <el-col :span="20" :offset="2">
              <el-radio v-for="(option) in JSON.parse(que.q_options)" v-model="answer[index]"
                        :label="option.text">{{option.text}}
              </el-radio>
            </el-col>
          </el-row>
          <el-row class="pd-l" v-if="que.q_titleType == 2">
            <el-col :span="20" :offset="2">
              <el-checkbox-group v-model="answer[index]">
                <el-checkbox v-for="(option) in JSON.parse(que.q_options)"
                             :label="option.text">
                </el-checkbox>
              </el-checkbox-group>
            </el-col>
          </el-row>
          <el-row class="pd-l" v-if="que.q_titleType == 3">
            <el-col :span="20" :offset="2">
              <el-input v-model="answer[index]"></el-input>
            </el-col>
          </el-row>
          <el-row class="pd-l" v-if="que.q_titleType == 4">
            <el-col :span="20" :offset="2">
              <el-input type="textarea" v-model="answer[index]"></el-input>
            </el-col>
          </el-row>
        </div>
      </div>
      <div v-if="wj_info.complete">
        <!--<el-row class="mg-tl">-->
          <!--<el-col :span="20" :offset="2">-->
            <!--<el-button type="primary" @click="completed()">完成问卷创建</el-button>-->
          <!--</el-col>-->
        </el-row>
      </div>
      <div v-else>
        <el-row class="mg-tl">
          <el-col :span="20" :offset="2">
            <el-button type="primary" @click="completed()">完成问卷创建</el-button>
            <el-button type="success" @click="show2=!show2">添加问题</el-button>
          </el-col>
        </el-row>

        <transition name="el-zoom-in-center">
          <el-row v-show="show2">
            <el-col :span="20" :offset="2">
              <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="questionSelect">
                <el-menu-item index="1">
                  <span slot="title">选择问题类型==></span>
                </el-menu-item>
                <el-menu-item index="2">
                  <i class="el-icon-menu"></i>
                  <span slot="title">单选题</span>
                </el-menu-item>
                <el-menu-item index="3">
                  <i class="el-icon-document"></i>
                  <span slot="title">多选题</span>
                </el-menu-item>
                <el-menu-item index="4">
                  <i class="el-icon-setting"></i>
                  <span slot="title">单行文本题</span>
                </el-menu-item>
                <el-menu-item index="5">
                  <i class="el-icon-setting"></i>
                  <span slot="title">多行文本题</span>
                </el-menu-item>
                <!--<el-menu-item index="6">-->
                  <!--<i class="el-icon-setting"></i>-->
                  <!--<span slot="title">填空题</span>-->
                <!--</el-menu-item>-->
              </el-menu>
            </el-col>
          </el-row>
        </transition>
      </div>
    </el-container>
  </div>
</template>

<script>
  import request from 'superagent'
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    data () {
      return {
        loading: false,
        activeIndex: '1',
        questionnaire: {},
        ques: {},
        answer: [],
        wj_info: {},
        answers: [],
        show2: false
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
      questionSelect(key, keyPath){
        switch (key) {
          case '1':
//            this.$router.push('/createQuestionnaire/singleChoice');
            break;
          case '2':
            this.$router.push({name: 'singleChoice', params: {id: this.$route.params.id}})
            break;
          case '3':
            this.$router.push({name: 'multipleChoice', params: {id: this.$route.params.id}})
            break;
          case '4':
            this.$router.push({name: 'singleLineText', params: {id: this.$route.params.id}})
            break;
          case '5':
            this.$router.push({name: 'multipleLineText', params: {id: this.$route.params.id}})
            break;
          case '6':
            this.$router.push({name: 'completion', params: {id: this.$route.params.id}})
            break;
        }
      },
      fetchData () {
        this.error = this.post = null
        this.loading = true
        // replace getPost with your data fetching util / API wrapper
        request
          .post('/api/test_paper')
          .send({
            wj_id: this.$route.params.id
          })
          .end((err, res) => {
            this.loading = false
            if (!err) {
              if (res.body.result == "success") {
                this.ques = res.body.ques
                this.wj_info = res.body.wj_info
                console.log(this.ques, "ques")
                for (var i = 0; i < res.body.ques.length; i++) {
                  this.answer[i] = [];
                }
              }
            }
          })
      },
      completed() {
        request
          .post('/api/complete')
          .send({
            wj_id: this.$route.params.id,
          })
          .end((err, res) => {
            if (res.body.result == "success") {
              this.$router.push('/myQuestionnaire');
            }
          })
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

<style lang="scss" rel="stylesheet/scss" scoped>

  .main-head {
    margin-bottom: 50px;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-container {
    height: 500px;
  }

  .title, .subtitle {
    text-align: center;
  }

  .title {
    font-size: larger;
    font-weight: bold;
  }

  .el-menu-demo {
    margin-bottom: 20px;
  }

  .content {
    text-align: left;
  }

  .mg-t {
    margin-top: 20px;
    margin-bottom: 10px;
  }

  .mg-tl {
    text-align: center;
    margin-top: 60px;
    margin-bottom: 20px;
  }

  .pd-l {
    padding-left: 30px;
  }

</style>
