<template>
  {{ pinfo }}
  <div>
    <div v-for="item in review_list">
      {{ item }}
    </div>
  </div>
  <router-link to="/">back</router-link>
</template>
<script>
import { defineComponent, onMounted, reactive, ref } from "vue";
import { useRoute } from "vue-router";
import { api } from "boot/axios";

export default defineComponent({
  setup(props, ctx) {
    //router是全局路由对象，route= userRoute()是当前路由对象
    let route = useRoute();
    const type = route.params.type;
    const pid = route.params.pid;
    const check_flag = route.params.check_flag;

    //请求景点信息数据
    const pinfo = reactive({
      pname: "", //产品名
      pdesc: "", //产品介绍
      pfeatures: "", //产品特点
      poffer: "", //产品供应商
      ppeoplenum: "", //产品消费人数
      ptotalnum: "", //总评论数
    });

    const getinfo = () => {
      let post_data = { type: type.value, pid: pid.value };
      api.post("/getinfo/", post_data).then((res) => {
        pinfo.pname = res.data.pname;
        pinfo.pdesc = res.data.pdesc;
        pinfo.features = res.data.pfeatures;
        pinfo.poffer = res.data.poffer;
        pinfo.ppeoplenum = res.data.ppeoplenum;
      });
    };

    //请求评论数据
    const review_list = ref("");
    const pic_list=ref("")
    const getreview = () => {
      let post_data = { type: type.value, pid: pid.value };
      api.post("/getreview/", post_data).then((res) => {
        pinfo.ptotalnum = res.data.totalnum;
        review_list.value = res.data.reviewlist;
        pic_list.value= res.data.piclist;
        console.log(res);
      });
    };

    onMounted(() => {
      if (check_flag) {
        getinfo();
        getreview();
      } else {
        console.log("check_flag is false");
      }
    });

    return {
      getinfo,
      pinfo,
      getreview,
      review_list,
    };
  },
});
</script>
