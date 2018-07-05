<template>
  <div class="create_title">
    <el-header class="main-head">
      创建标题
    </el-header>
    <div class="q_title">
      <el-row class="title">
        <el-col :span="20" :offset="2">
          主标题：
          <el-input class="title" v-model="title" placeholder="问卷标题" required></el-input>
        </el-col>

      </el-row>
      <el-row class="disc">
        <el-col :span="20" :offset="2">
          添加描述：
          <el-input v-model="subtitle"
                    placeholder="描述"></el-input>
        </el-col>
      </el-row>
    </div>
    <el-row>
      <el-col :span="4" :offset="10" class="confirm">
        <el-button type="success" @click="confirm">确认创建</el-button>
      </el-col>
    </el-row>

  </div>
</template>

<script type="text/ecmascript-6">
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default{
    data() {
      return {
        title: '',
        subtitle: ''
      }
    },
    methods: {
      confirm: function () {
        console.log("test")
        const questionnaireInfo = {
          title: this.title,
          subtitle: this.subtitle,
          self: this
        }
        this.$store.dispatch('create_title', questionnaireInfo)
      },
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

  .title {
    margin-bottom: 10px;
  }

  .disc {
    margin-bottom: 20px;
  }

  .confirm {
    text-align: center;
  }
</style>
