<template>
  <div class="main-container">
        <div class="main-content">
          <router-view/>
        </div>
      </el-container>
    </el-container>
  </div>
</template>

<script type="text/ecmascript-6">
  import {mapState, mapGetters, mapActions} from 'vuex'
  export default {
    name: 'App',
    data() {
      return {
        activeIndex: '1',
      }
    },
    computed: {
      // 使用对象展开运算符将 getter 混入 computed 对象中
      ...mapGetters([
        'question_no'
      ])
    },
    methods: {
      open() {
        this.$alert('继续上次', '标题名称', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'info',
              message: `action: ${ action }`
            });
          }
        });
      },
//      questionSelect(key, keyPath){
//        switch (key) {
//          case '1':
//            this.$router.push('/createQuestionnaire/singleChoice');
//            break;
//          case '2':
//            this.$router.push('/createQuestionnaire');
//            break;
//          case '3':
//            this.$router.push('/createQuestionnaire/multipleChoice');
//            break;
//          case '4':
//            this.$router.push('/createQuestionnaire/singleLineText');
//            break;
//          case '5':
//            this.$router.push('/createQuestionnaire/multipleLineText');
//            break;
//          case '6':
//            this.$router.push('/createQuestionnaire/completion');
//            break;
//        }
//      },
    },
  }
</script>

<style lang="scss" rel="stylesheet/scss" scoped>
  .main-head {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }


  .aside-nav {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .main-content {
    background-color: #E9EEF3;
    color: #333;
    text-align: left;
    height: 800px;
  }

</style>
