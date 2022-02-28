<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 15:41:20
 * @LastEditTime: 2022-02-28 16:42:13
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\submit.vue
-->
<template>
  <div class="form">
    <q-toolbar class="bg-secondary text-white rounded-borders row">
      <q-select
        filled
        v-model="type"
        :options="type_options"
        label="网站类型"
        label-color="white"
        class="col-4"
      />
      <q-input
        dark
        dense
        standout
        v-model="pid"
        input-class="text-right"
        class="col-6 q-mr-sm"
      >
        <template v-slot:append>
          <q-icon
            v-if="pid != ''"
            name="clear"
            class="cursor-pointer"
            @click="pid = ''"
          />
        </template>
      </q-input>
      <q-space />
      <q-btn round label="Go" class="text-weight-medium" @click="spyder_go" />
    </q-toolbar>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { api } from "boot/axios";
export default defineComponent({
  name: "submit",
  setup() {
    const type = ref("");
    const type_options = ["携程", "马蜂窝"];
    const pid = ref("");

    //请求爬虫
    const getinfo = () => {
        let post_data={"type":type.value,"pid":pid.value}
      api.post("/getinfo");
    };

    return {
      type,
      type_options,
      pid,
    };
  },
});
</script>
