<template>
  <div class="header">
    <div class="content-wrapper">
      <div class="avatar">
        <img :src="seller.avatar" height="64" width="64">
      </div>
      <div class="content">
        <div class="title">
          <span class="brand"></span>
          <span class="name">{{ seller.name }}</span>
        </div>
        <div class="description">
          {{seller.description}}/{{seller.deliveryTime}}分钟送达
        </div>
        <div v-if="seller.supports" class="support">
          <span class="icon" :class="classMap[seller.supports[0].type]"></span>
          <span class="text">{{seller.supports[0].description}}</span>
        </div>

      </div>
      <div v-if="seller.supports" class="support-count" @click="showDetail">
        <span class="count">{{seller.supports.length}}个</span>
        <i class="icon-keyboard_arrow_right"> > </i>
      </div>
    </div>
    <div class="bulletin-wrapper">
      <span class="bulletin-title"></span><span class="bulletin-text">{{seller.bulletin}}</span>
      <i class="icon-keyboard_arrow_right"> > </i>
    </div>
    <div class="background">
      <img :src="seller.avatar" width="100%" height="100%">
    </div>
    <div v-show="detailShow" class="detail">
      <div class="detail-wrapper clearfix">
        <div class="detail-main"></div>
      </div>
      <div class="detail-close">
        <i class="fa fa-camera-retro"></i>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      seller: {
        type: Object
      }
    },
    data () {
      return {
        detailShow: false
      }
    },
    methods: {
      showDetail () {
        this.detailShow = true
      }
    },
    created () {
      this.classMap = ['decrease', 'discount', 'special', 'invoice', 'guarantee']
    }
  }
</script>


<style lang="scss" type="text/scss">
  @import "../../common/scss/mixin";

  .header {
    position: relative;
    overflow: hidden;
    color: #fff;
    background: rgba(7, 17, 27, 0.5);
    .content-wrapper {
      padding: 24px 12px 18px 24px;
      font-size: 0;
      .avatar {
        display: inline-block;
      }
      .content {
        display: inline-block;
        margin-left: 16px;
        font-size: 14px;
        .title {
          margin: 2px 0 8px 0;
          .brand {
            display: inline-block;
            width: 30px;
            height: 18px;
            @include bg-image('brand');
            background-size: 30px 18px;
            background-repeat: no-repeat;
          }
          .name {
            vertical-align: top;
            margin-left: 6px;
            font-size: 16px;
            height: 18px;
            font-weight: bold;
          }
        }
      }
      .support-count {
        position: absolute;
        right: 24px;
        bottom: 48px;
        padding: 0 8px;
        height: 24px;
        line-height: 24px;
        border-radius: 14px;
        background: rgba(0, 0, 0, 0.2);
        text-align: center;
        font-weight: 200;
        font-size: 12px;
      }
      .description {
        font-size: 12px;
        font-weight: 100;
        line-height: 12px;
      }
      .support {
        .icon {
          display: inline-block;
          width: 12px;
          height: 12px;
          margin-right: 4px;
          background-size: 12px 12px;
          background-repeat: no-repeat;
          &.decrease {
            @include bg-image('decrease_1');
          }
          &.discount {
            @include bg-image('discount_1');
          }
          &.special {
            @include bg-image("special_1");
          }
          &.guarantee {
            @include bg-image('guarantee_1');
          }
          &.invoice {
            @include bg-image('invoice_1');
          }
        }
        .text {
          line-height: 12px;
          font-size: 10px;
          font-weight: 100;
        }
      }
    }
    .bulletin-wrapper {
      position: relative;
      height: 28px;
      line-height: 28px;
      padding: 0 22px 0 12px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      background: rgba(7, 17, 27, 0.2);
      .bulletin-title {
        display: inline-block;
        vertical-align: top;
        margin-top: 8px;
        width: 22px;
        height: 12px;
        @include bg-image("bulletin");
        background-size: 22px 12px;
      }
      .bulletin-text {
        vertical-align: top;
        margin: 0 4px;
        font-size: 10px;
        font-weight: 100;
      }
      .icon-keyboard_arrow_right {
        position: absolute;
        font-size: 10px;
        right: 12px;
        top: 8px;
      }
    }
    .background {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
      filter: blur(10px);
    }
    .detail {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 100;
      overflow: auto;
      background: rgba(7, 17, 27, 0.8);
      .detail-wrapper{
        min-height: 100%;
        .detail-main{
          margin-top: 64px;
          padding-bottom: 64px;
        }
        .detail-close{
          position: relative;
          width: 32px;
          height: 32px;
          margin: -64px auto 0 auto;
          clear: both;
          font-size: 32px;
        }
      }
    }
  }
</style>
