<template>
  <div id="app">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
             background-color="#545c64"
             text-color="#fff"
             active-text-color="#ffd04b">>
      <el-menu-item index="1">主页</el-menu-item>
      <el-menu-item index="2">创建问卷</el-menu-item>
      <el-menu-item index="3">我的问卷</el-menu-item>
      <!--<el-menu-item index="4">问卷中心</el-menu-item>-->
      <el-menu-item index="5" v-if="!isLogin" class="loginModule">登录</el-menu-item>
      <el-menu-item index="6" v-if="!isLogin" class="loginModule">注册</el-menu-item>
      <el-menu-item index="7" v-if="isLogin" class="loginModule">登出</el-menu-item>
      <el-menu-item index="8" v-if="isLogin" class="loginModule">{{username}}</el-menu-item>
    </el-menu>
    <router-view/>
  </div>
</template>

<script>
  import {mapState, mapGetters, mapActions} from 'vuex'
  import request from 'superagent'
  export default {
    name: 'App',
    data() {
      return {
        activeIndex: '1',
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
    computed: {
      // 使用对象展开运算符将 getter 混入 computed 对象中
      ...mapGetters([
        'isLogin',
        'username'
      ]),
    },
    methods: {
      fetchData () {
        request
          .post('/api/isLogin')
          .end((err, res) => {
            if (!err) {
              if (res.body.result == "success") {
                username: res.body.username
                const userInfo = {
                  isLogin: true,
                  username: res.body.username
                }
                this.$store.dispatch('login_user', userInfo);
              }
            }
          })
      },
      handleSelect(key, keyPath)
      {
        switch (key) {
          case '1':
            this.$router.push('/');
            break;
          case '2':
            this.$router.push('/createQuestionnaire');
            break;
          case '3':
            this.$router.push({path: '/myQuestionnaire'});
            break;
          case '5':
            this.$router.push('/login');
            break;
          case '6':
            this.$router.push('/register');
            break;
          case '7':
            this.$store.dispatch('logout_user');
            break
        }
      }
      ,
    },
  }
</script>

<style lang="scss" rel="stylesheet/scss" scoped>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  a {
    text-decoration: none;
  }

  .loginModule {
    float: right;
  }

</style>
