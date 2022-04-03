<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 15:41:20
 * @LastEditTime: 2022-03-04 15:56:52
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\submit.vue
-->
<template>
  <div class="form flex row ">
    <div class="optionBar col-sm-12 col-md-12 col-lg-3 flex flex-center">
      <q-option-group
        v-model="type"
        :options="type_options"
        inline
        dense
        keep-color
        color="warning"
      />
    </div>
    <div class="inputBar item col-sm-12 col-md-12 col-lg-5 flex flex-center">
      <q-input outlined v-model="pid" input-class="text-right text-white" placeholder="输入产品id">

      </q-input>
    </div>
    <div class="submitBtn item col-sm-12 col-md-12 col-lg-2 flex flex-center">
      <q-btn color="secondary" @click="spyder_go">Go</q-btn>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.form {
  .optionBar {
    margin-bottom: 10px;
  }

  .item {
    @media (max-width: 800px) {
    margin-bottom: 10px;
    height: 40px;
    width: 100%;

  }
    margin-bottom: 10px;
    height: 40px;

    :first-child {
      width: 100%;
      height: 100%;
    }
  }
}
</style>
<script>
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
export default defineComponent({
  name: "submit",
  setup(props, ctx) {
    const type = ref("");
    const type_options = [
      {
        label: "携程",
        value: "ctrip",
      },
      {
        label: "马蜂窝",
        value: "mfw",
        disable: true,
      },
    ];
    const pid = ref("");
    const e_flag = ref(false);

    let router = useRouter();

    const spyder_go = () => {
      if ((type.value === "") || (pid.value === "")) {
        e_flag.value = true;
        ctx.emit("e_flag", e_flag.value);
      } else {
        router.push({
          name: "end",
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
