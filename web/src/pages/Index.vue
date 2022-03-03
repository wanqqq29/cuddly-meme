<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-03-03 16:03:09
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\pages\Index.vue
-->
<template>
  <q-dialog rounded v-model="e_flag" position="top">
    <q-card
      style="width: 350px; height: 5rem; font-size: 1.5rem"
      class="flex flex-center text-center bg-secondary text-white text-weight-bold"
    >
      请输入正确的网站与产品id
    </q-card>
  </q-dialog>
  <q-page class="flex flex-center column text-white">
    <div class="title">
      <h2 class="text-weight-medium text-center">
        旅游景点评论分析系统<br />👋Hi~
      </h2>
    </div>
    <submit class="submit" @e_flag="get_e_flag" />
  </q-page>
</template>

<style lang="scss" scoped>
.err_ {
  z-index: 3;
  position: absolute;
  top: 0;
  width: 50%;
  left: 50%;
  transform: translate(-50%);
}
.title {
  margin-top: -15%;
}
.submit {
  @media (min-width: 992px) {
    width: 30%;
  }
  width: 90%;
}
</style>
<script>
import { defineComponent, ref } from "vue";
import submit from "components/submit.vue";
export default defineComponent({
  name: "PageIndex",
  components: {
    submit,
  },
  setup() {
    const e_flag = ref(false);
    const get_e_flag = (e) => {
      e_flag.value = e;
    };
    const close_e = () => {
      e_flag.value = false;
    };
    return {
      get_e_flag,
      close_e,
      e_flag,
    };
  },
});
</script>
