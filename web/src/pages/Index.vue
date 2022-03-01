<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-03-01 09:07:36
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\pages\Index.vue
-->
<template>
  <q-page class="flex flex-center column bg-indigo-10 text-white">
    <div class="title">
      <h2 class="text-weight-medium text-center">
        旅游景点评论分析系统<br />👋Hi~
      </h2>
    </div>
    <submit class="submit"/>
  </q-page>
</template>

<style lang="scss" scoped>
.title{
  margin-top: -15%;
}
.submit{
  @media (min-width:992px) {
    width: 30%;
  }
  width: 90%;
}
</style>
<script>
import { defineComponent } from "vue";
import submit from "components/submit.vue";
export default defineComponent({
  name: "PageIndex",
  components: {
    submit,
  },
});
</script>
