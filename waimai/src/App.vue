<template>
  <div id="app">
    <v-header :seller="seller"></v-header>
    <div class="tab">
      <div class="tab-item">
        <router-link to="/goods">商品</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/ratings">评论</router-link>
      </div>
      <div class="tab-item">
        <router-link to="/seller">商家</router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import header from './components/header/header.vue'

  const ERR_OK = 0

  export default {
    data () {
      return {
        seller: {}
      }
    },
    created () {
      this.$http.get('api/seller').then((response) => {
        response = response.body
        console.log(response.errno)
        console.log(ERR_OK)
        if (response.errno === ERR_OK) {
          console.log('test')
          console.log(response)
          console.log(response.good)
          this.seller = response.good
          console.log(this.seller)
        }
      })
    },
    components: {
      'v-header': header
    }
  }
</script>

<style lang="scss" type="text/scss">
  @mixin border-1px($color) {
    border-bottom: 1px solid $color;
    position: relative
  }

  .tab {
    display: flex;
    width: 100%;
    height: 40px;
    line-height: 40px;
    border-bottom: 1px solid rgba(7, 178, 27, 0.1);
    position: relative;
    /*<!--@include boder-1px(rgba(7,12,27,0.1));-->*/
    .tab-item {
      flex: 1;
      text-align: center;
    }
  }
</style>
