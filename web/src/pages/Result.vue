<!--
 * @Author: wanqqq29
 * @Date: 2022-03-01 09:13:54
 * @LastEditTime: 2022-03-03 10:26:28
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\pages\result.vue
-->
<template>
  {{ pinfo }}
  <div>
    <div v-for="item in review_list">
      {{ item }}
    </div>
    {{ charts_data }}
  </div>

  <pie-chart :pieData="charts_data.charts.pie" />
  <router-link to="/">back</router-link>
</template>
<script>
import { defineComponent, onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api } from "boot/axios";
import PieChart from "../components/charts/PieChart.vue";

export default defineComponent({
  components: { PieChart },

  setup(props, ctx) {
    //router是全局路由对象，route= useRoute()是当前路由对
    let router = useRouter();
    let route = useRoute();
    const post_data = { type: route.params.type, pid: route.params.pid };
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
      api.post("/getInfo/", post_data).then((res) => {
        pinfo.pname = res.data.pname;
        pinfo.pdesc = res.data.pdesc;
        pinfo.features = res.data.pfeatures;
        pinfo.poffer = res.data.poffer;
        pinfo.ppeoplenum = res.data.ppeoplenum;
      });
    };

    //请求评论数据
    const review_list = ref("");
    const pic_list = ref("");
    const getreview = () => {
      api.post("/getReview/", post_data).then((res) => {
        pinfo.ptotalnum = res.data.totalnum;
        review_list.value = res.data.reviewlist;
        pic_list.value = res.data.piclist;
      });
    };

    //获取情感分析图表数据
    const charts_data = reactive({
      score: "", //
      charts: {
        pie: "", //好评率
        wordCloud: "", //词云
        bar: "", //柱状图
      },
    });
    const getSentiments2 = () => {
      api
        .post("/getSentiments2", post_data)
        .then((res) => {
          charts_data.charts.pie = res.data.charts.pie;
          charts_data.charts.wordCloud = res.data.charts.wordCloud;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    onMounted(() => {
      if (
        check_flag |
        (post_data.type != undefined) |
        (post_data.pid != undefined)
      ) {
        getinfo();
        getreview();
        getSentiments2();
      } else {
        router.push("/");
      }
    });

    return {
      post_data,
      getinfo,
      pinfo,
      getreview,
      review_list,
      charts_data,
      getSentiments2,
    };
  },
});
</script>
