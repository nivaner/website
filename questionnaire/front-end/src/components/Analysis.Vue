<template>
  <div class="analysis">
    <el-row>
      <el-col :span="20" :offset="2">
        <div class="main-title">{{wj_info.title}}</div>
        <div class="subtitle">{{wj_info.subtitle}}</div>
        <div v-for="(result,index) in results">
          <div class="title">题目{{index+1}}：{{result.title}}</div>
          <div v-if="result.title_type === 1">
            <div :id="gernerateId(index)"  class="pic" ></div>
            <!--<el-button @click="draw(index,result.answer.answer,result.answer.option)">show</el-button>-->
          </div>
          <div v-else-if="result.title_type === 2">
            <div :id="gernerateId(index)" class="pic"></div>
            <!--<el-button @click="draw(index,result.answer.answer,result.answer.option)">show</el-button>-->
          </div>
          <div v-else>
            <el-table
              :data="result.answer.answer"
              class="table">
              <el-table-column
                prop="id"
                label="编号"
                width="180">
              </el-table-column>
              <el-table-column
                prop="name"
                label="文本答案"
                width="420">
              </el-table-column>
            </el-table>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/ecmascript-6">
  import request from 'superagent'
  import {mapState, mapGetters, mapActions} from 'vuex'
  import echarts from 'echarts'
  export default {
    data () {
      return {
        loading: false,
        results: [],
        wj_info: {}
      }
    },

    created () {
      // 组件创建完后获取数据，
      // 此时 data 已经被 observed 了
      this.fetchData();
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
          .post('/api/analysis')
          .send({
            wj_id: this.$route.params.id
          })
          .end((err, res) => {
            this.loading = false
            if (!err) {
              if (res.body.result == "success") {
                this.results = res.body.datas
                this.wj_info = res.body.wj_info
              }
            }
          })
      },
//      draw(id,  seriesData, xAxisData){
//        var str = "grow_" + id
//        var myChart = echarts.init(document.getElementById(str));
//        // 绘制图表
//        myChart.setOption({
//          title: {
//            text: this.results[i].title
////            text: 'ECharts 入门示例'
//          },
//          tooltip: {},
//          toolbox: {
//            show: true,
//            feature: {
//              mark: {
//                show: true
//              },
//              dataView: {
//                show: true,
//                readOnly: false
//              },
//              magicType: {
//                show: true,
//                type: ['line', 'bar', 'pie']
//              },
//              restore: {
//                show: true
//              },
//              saveAsImage: {
//                show: true
//              }
//            }
//          },
//          xAxis: {
//            data: xAxisData
//          },
//          yAxis: {},
//          series: [{
//            name: '销量',
//            type: 'bar',
//            data: seriesData
//          }]
//        });
//      },
      gernerateId(index)
      {
        return "grow_" + index
      }
    },
    updated() {
      for(var i=0;i<this.results.length;i++){
        if(this.results[i].title_type === 1 || this.results[i].title_type === 2){
          var str = "grow_" + i
          var myChart = echarts.init(document.getElementById(str));
          console.log(myChart)
          myChart.setOption({
            title: {
              text: this.results[i].title
            },
            tooltip: {},
            toolbox: {
              show: true,
              feature: {
                mark: {
                  show: true
                },
                dataView: {
                  show: true,
                  readOnly: true
                },
                magicType: {
                  show: true,
                  type: ['line', 'bar', 'pie']
                },
                restore: {
                  show: true
                },
                saveAsImage: {
                  show: true
                }
              }
            },
            xAxis: {
              data: this.results[i].answer.option
            },
            yAxis: {},

            series: [{
              type: 'bar',
              data: this.results[i].answer.answer
            }]
          });
        }
      }
    }
  }
</script>

<style lang="scss" rel="stylesheet/scss">
  .main-title, .subtitle {
    text-align: center;
  }

  .main-title {
    font-size: larger;
    font-weight: bold;
    margin-top: 40px;
  }
  .subtitle{
    margin-top: 5px;
    margin-bottom: 30px;
  }
  .title{
    text-align: left;
  }
  .pic{
    width: 600px;
    height: 400px;
    margin: 20px auto 0;
  }
  .table{
    width: 600px;
    margin: 20px auto 0;
  }
</style>
