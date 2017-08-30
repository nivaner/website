<template>
  <div id="app">
    <v-header></v-header>
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

<script>
  import header from './components/header/header.vue'

  export default {
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
    /*border-bottom: 1px solid rgba(7,178,27,0.1);*/
    @include boder-1px(rgba(7,12,27,0.1));
    .tab-item {
      flex: 1;
      text-align: center;
    }
  }
</style>
