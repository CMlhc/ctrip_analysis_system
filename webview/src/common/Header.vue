<template>
  <div>
    <router-link to="/">
      <p>携程爬虫首页</p>
    </router-link>
    <router-link to="/comment">
      <p>基于aspect的情感分析</p>
    </router-link>
    <router-link to="/crawler">
      <p>景点持续爬虫</p>
    </router-link>
    <router-link to="/analysis">
      <p>文本情感分析</p>
    </router-link>
    <router-link to="/mycrawler">
      <p>爬虫例子</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CommonHeader'
}

</script>

<style lang="scss" scoped>
  div {
    text-align: center;
  }

  p {
    display: inline-block;
    color: #fff;
    font-size: .3rem;
    padding: .26rem .24rem;
    -webkit-font-smoothing: antialiased;
    text-align: center;
  }

  p:hover {
    color: #4fb6ff;
  }

</style>
