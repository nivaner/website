<template>
  <div class="single-choice">
    <el-header class="main-head">
      单选题
    </el-header>
    <el-row>
      <el-col :span="20" :offset="2">
        <div class="mg-b">
          问题：
          <el-input class="title" v-model="q_title" placeholder="单选题目为"></el-input>
        </div>
        <div v-for="option in options">
          <div class="mg-b">选项{{option.id}}:
            <el-input class="title" v-model="option.text" placeholder="选项为"></el-input>
          </div>
        </div>
      </el-col>
    </el-row>
    <div class="buttons">
      <el-button type="primary" @click="addOption()">添加选项</el-button>
      <el-button type="primary" @click="reduceOption()">删除选项</el-button>
      <el-button type="success" @click="complete()">完成并预览</el-button>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data () {
      return {
        q_title: '',
        options: [{
          id: 'A',
          text: ''
        }],
        item: '',
        option_type: 1
      }
    },
    created () {
    },
    watch: {
    },
    methods: {
      addOption () {
        var alphabe = ["A", "B", "C", "D", "E", "F", "G",
          "H", "I", "J", "K", "L"]
        this.options.push({id: alphabe[this.options.length], text: ''})
        console.log(this.options, "click")
      },
      reduceOption () {
        if(this.options.length > 1){
          this.options.pop()
        }
      },
      complete () {
        console.log(this.q_title, "this.title")
        const questionInfo = {
          q_title: this.q_title,
          options: this.options,
          option_type: this.option_type,
          wj_id: this.$route.params.id,
          self: this
        }
        console.log(questionInfo)
        this.$store.dispatch('create_question', questionInfo)
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
  .mg-b{
    margin-bottom: 20px;
  }
  .buttons{
    margin-top: 40px;
    text-align: center;
  }
</style>
