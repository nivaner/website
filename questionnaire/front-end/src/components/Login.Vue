<template>
  <div class="login">
    <el-row>
      <el-col :span="20" :offset="2">
        <el-form :model="loginForm"
                 status-icon
                 ref="loginForm"
                 label-width="100px">
          <el-form-item label="用户名" prop="nickname">
            <el-input v-model="loginForm.nickname"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass">
            <el-input type="password" v-model="loginForm.pass" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/ecmascript-6">
  import {mapState, mapGetters, mapActions} from 'vuex'
  import request from 'superagent'
  export default {
    data() {
      return {
        loginForm: {
          pass: '',
          nickname: '',
        },
      };
    },
    computed: {
      // 使用对象展开运算符将 getter 混入 computed 对象中
      ...mapGetters([
        'isLogin',
      ])
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if(this.loginForm.nickname == ""){
            alert("请输入用户名")
          }
          if(this.loginForm.pass == ""){
            alert("请输入密码")
          }
          if (valid) {
            request
              .post('/api/login')
              .send({
                nicknameValue: this.loginForm.nickname,
                passwordValue: this.loginForm.pass,
              })
              .end((err, res) => {
                if (!err) {
                  console.log(res)
                  if (res.body.result == "success") {
                    const userInfo = {
                      isLogin: true,
                      username: res.body.username
                    }
                    this.$store.dispatch('login_user', userInfo);
                    this.$router.push('/myQuestionnaire');
                  } else {
                    alert("登录失败")
                  }
                }
              })
          }
          else {
            return false;
          }
        });
      }
    }
  }
</script>

<style lang="scss" rel="stylesheet/scss" scoped>
  .el-row{
    margin-top: 40px;
  }
</style>
