<template>
  <div class="answer">
    <div v-if="wj_info.release_date">
      <div v-if="wj_info.collect_date">
        感谢参与！
      </div>
      <div v-else>
        <el-row>
          <h3>{{wj_info.title}}</h3>
          <h4>{{wj_info.subtitle}}</h4>
        </el-row>
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

        <el-button type="primary" class="submit" @click="submit()">提交问卷</el-button>
      </div>
    </div>
    <div v-else>
      问卷还未创建完毕或者不存在
    </div>

  </div>
</template>

<script type="text/ecmascript-6">
  import request from 'superagent'
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    data () {
      return {
        loading: false,
        wj_info: {},
        ques: {},
        answer: [],
        answers: []
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
                for(var i = 0; i <res.body.ques.length; i++){
                  this.answer[i] = [];
                }
              }
            }
          })
      },
      submit() {
        for(var i =0; i <this.ques.length; i++){
          var ans = {};
          ans["id"] = this.ques[i].id;
          ans["type"] = this.ques[i].q_titleType;
          ans["title"] = this.ques[i].q_title;
          ans["text"] = this.answer[i];
          this.answers.push(ans);
        }
        console.log(this.answers)
//        console.log(this.answers,"test");
        request
          .post('/api/answer')
          .send({
            wj_id: this.$route.params.id,
            wj_answer: this.answers
          })
          .end((err, res) => {
            if (res.body.result == "success") {
              this.$router.push('/answerSuccess');
            }
          })
      }
    },
    filters: {
      jsonData: function (value) {
        if (!value) return ''
//        console.log(value)
//        console.log(JSON.parse(value))
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
  .content{
    text-align: left;
  }
  .mg-t{
    margin-top: 20px;
    margin-bottom: 10px;
  }
  .pd-l{
    padding-left: 30px;
  }
  .submit{
    margin-top: 30px;
  }
</style>
