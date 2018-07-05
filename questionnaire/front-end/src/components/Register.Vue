<template>
  <div class="register">
    <el-row>
      <el-col :span="20" :offset="2">
        <el-form :model="registerForm"
                 status-icon :rules="rules2"
                 ref="registerForm"
                 label-width="100px"
                 class="demo-ruleForm">
          <el-form-item label="用户名" prop="nickname">
            <el-input v-model="registerForm.nickname"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass">
            <el-input type="password" v-model="registerForm.pass" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPass">
            <el-input type="password" v-model="registerForm.checkPass" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('registerForm')">提交</el-button>
            <el-button @click="resetForm('registerForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>

  </div>
</template>

<script type="text/ecmascript-6">
  import request from 'superagent'

  export default {
    data() {
      var checkNickname = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('用户名不能为空'));
        }
        setTimeout(() => {
          if (true) {
            callback(new Error('请输入数字值'));
          } else {
            if (true) {
              callback(new Error('必须年满18岁'));
            } else {
              callback();
            }
          }
        }, 1000);
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.registerForm.checkPass !== '') {
            this.$refs.registerForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.registerForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        registerForm: {
          pass: '',
          checkPass: '',
          nickname: ''
        },
        rules2: {
          pass: [
            {validator: validatePass, trigger: 'blur'}
          ],
          checkPass: [
            {validator: validatePass2, trigger: 'blur'}
          ]
        },
      };
    },
    computed: {
      // 使用对象展开运算符将 getter 混入 computed 对象中
//      ...mapGetters([
//        'isRegister',
//      ])
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log("register user now" + this.isRegister)
            const userInfo = {
              nickname: this.registerForm.nickname,
              password: this.registerForm.pass
            }
            request
              .post('/api/register')
              .send({
                nicknameValue: userInfo.nickname,
                passwordValue: userInfo.password,
              })
              .end((err, res) => {
                if (!err) {
                  alert("注册成功，登录跳转首页")
                  if(res.body.result == "success"){
                    request
                      .post('/api/login')
                      .send({
                        nicknameValue: this.registerForm.nickname,
                        passwordValue: this.registerForm.pass,
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
                }
              })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }
</script>

<style lang="scss" rel="stylesheet/scss" scoped>
  .register {
    margin-top: 50px;
  }
</style>
