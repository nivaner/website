<template>
  <div class="hello">
    <div class="jumbotron text-center">
      <h3>Welcome</h3>
      <h1>问卷调查</h1>
      <p>基于H5的问卷调查系统!</p>
    </div>
    <el-row>
      <el-col :span="12">
            <h3>创建问卷</h3>
            <p>自定义创建问卷</p>
            <p>创建自己想要的问卷</p>
      </el-col>
      <el-col :span="12">
        <h3>我的问卷</h3>
        <p>管理问卷发布回收</p>
        <p>回收结果数据可视化</p>
      </el-col>
      <!--<el-col :span="8">-->
        <!--<h3>问卷中心</h3>-->
        <!--<p>查看所有问卷</p>-->
        <!--<p>教你快速创建问卷</p>-->
      <!--</el-col>-->
    </el-row>
  </div>

</template>

<script>
  export default {
    name: 'Home',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .jumbotron {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
    background-color: #e9ecef;
    border-radius: .3rem;
  }
</style>
