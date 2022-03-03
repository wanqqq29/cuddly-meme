<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 15:41:20
 * @LastEditTime: 2022-03-01 15:04:04
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
import { useRouter } from "vue-router";
export default defineComponent({
  name: "submit",
  setup(props, ctx) {
    const type = ref("");
    const type_options = ["携程", "马蜂窝"];
    const pid = ref("");
    const e_flag = ref(false)
    
    let router = useRouter();

    const spyder_go = () => {
      if ((type.value == "") | (pid.value == "")) {
        e_flag.value=true
        ctx.emit('e_flag',e_flag.value)
        console.log(e_flag.value);
      } else {
        router.push({
          name: "result",
          params: {
            type: type.value,
            pid: pid.value,
            check_flag: true,
          },
        });
      }
    };

    return {
      type,
      type_options,
      pid,
      e_flag,
      spyder_go,
    };
  },
});
</script>
