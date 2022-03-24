<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-03-04 15:44:52
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\layouts\MainLayout.vue
-->
<template>
  <q-layout view="hHh lpR fFf" class="mLayout">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<style lang="scss">
.body--light {
  background: linear-gradient(
    90deg,
    rgba(106, 17, 203, 1) 0%,
    rgba(37, 117, 252, 1) 100%
  );
  .q-dialog {
    background: linear-gradient(
      90deg,
      rgba(59, 4, 117, 0.6) 0%,
      rgba(7, 68, 173, 0.6) 100%
    );
  }
  .darkBtn {
    color: black;
  }
}

.body--dark {
  .darkBtn {
    color: white;
  }
}
</style>
<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {},

  setup() {
    return {};
  },
});
</script>
