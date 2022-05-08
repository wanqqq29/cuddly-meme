<!--
 * @Author: wanqqq29
 * @Date: 2022-03-03 13:47:46
 * @LastEditTime: 2022-03-03 16:11:06
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\charts\barChart.vue
-->
<template>
  <div id="bar" ref="barDom" style="height: 250px"></div>
</template>

<script>
import { onMounted, reactive, ref, watchEffect } from "vue";
import * as echarts from "echarts/core";
import {
  TitleComponent,
  GridComponent,
  LegendComponent,
} from "echarts/components";
import { BarChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
echarts.use([
  TitleComponent,
  GridComponent,
  LegendComponent,
  BarChart,
  CanvasRenderer,
]);

export default {
  props: {
    barData: Object,
  },
  name: "bar",

  setup(props) {
    const bar_data = reactive({
      type: "",
      x: "",
      y: "",
      total: "",
    });
    const barDom = ref(null);
    const draw = () => {
      const barChart = echarts.init(barDom.value);
      window.onresize = () => {
        barChart.resize();
      };
      barChart.setOption({
        tooltip: {
          trigger: "item",
          formatter: "{a}:{c}",
        },
        title: {
          text: "1-12月客流量",
          left: 19,
          top: 15,
          textStyle: {
            color: "#fff",
          },
        },
        color: ["#4C98FB", "#83CCE7"],
        legend: {
          top: 10,
          left: 200,
          itemWidth: 10,
          itemHeight: 10,
          // padding: [5, 10],
          textStyle: {
            fontSize: 14,
            color: "#96A4F4",
            padding: [3, 0, 0, 0],
          },
          data: bar_data.type,
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "13%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          axisLabel: {
            color: "#96A4F4",
          },
          axisLine: {
            lineStyle: {
              color: "#96A4F4",
            },
            width: 5,
          },
          axisTick: {
            show: false,
          },
          data: bar_data.x,
        },
        yAxis: {
          type: "value",
          axisLabel: {
            color: "#96A4F4",
          },
          axisLine: {
            lineStyle: {
              color: "#96A4F4",
            },
            width: 5,
          },
          axisTick: {
            show: false,
          },
          splitLine: {
            lineStyle: {
              color: "rgba(150, 164, 244, 0.3)",
            },
          },
        },
        dataZoom: [
          {
            show: true,
            height: 30,
            bottom: 10,
            start: 10,
            end: 80,
            handleIcon:
              "path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z",
            handleSize: "110%",
            handleStyle: {
              color: "#d3dee5",
            },
            textStyle: {
              color: "#fff",
            },
          },
          {
            type: "inside",
            show: true,
            height: 15,
            start: 111,
            end: 35,
          },
        ],
        series: [
          {
            name: "好评",
            type: "bar",
            stack: "总量",
            barWidth: "45%",
            data: bar_data.y.good,
          },
          {
            name: "差评",
            type: "bar",
            stack: "总量",
            barWidth: "45%",
            data: bar_data.y.bad,
          },
          {
            name: "总数",
            type: "line",
            symbol: "circle",
            itemStyle: {
              normal: {
                color: "#E07BCE",
                label: {
                  show: true,
                  position: "top",
                },
              },
            },
            data: bar_data.total,
          },
        ],
      });
    };

    watchEffect(async () => {
      const response = await props.barData;
      bar_data.type = response.type;
      bar_data.x = response.x;
      bar_data.y = response.y;
      bar_data.total = response.y.good.map((v, i) => v + response.y.bad[i]);
      draw();
    });

    return {
      barDom,
      bar_data,
    };
  },
};
</script>
