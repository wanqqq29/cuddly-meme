<!--
 * @Author: wanqqq29
 * @Date: 2022-03-02 11:00:56
 * @LastEditTime: 2022-03-03 10:26:08
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\charts\PieChart.vue
-->
<template>
  {{ pie_data }}
  <div id="pie" ref="chartDom" style="height: 300px"></div>
</template>
<script>
import * as echarts from "echarts/core";
import {
  TooltipComponent,
  LegendComponent,
  TitleComponent,
  PolarComponent,
} from "echarts/components";
import { PieChart, BarChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import { onMounted, ref, watchEffect } from "vue";
echarts.use([
  TooltipComponent,
  LegendComponent,
  TitleComponent,
  PolarComponent,
  PieChart,
  BarChart,
  CanvasRenderer,
  LabelLayout,
]);

export default {
  props: {
    pieData: String,
  },
  name: "pie",
  setup(props, ctx) {
    const pie_data = ref("");
    const chartDom = ref(null);
    const draw = () => {
      const myChart = echarts.init(chartDom.value);
      window.onresize = function () {
        myChart.resize();
      };
      myChart.setOption(
        {
          title: [
            {
              text: "好评率",
              x: "center",
              top: "55%",
              textStyle: {
                color: "#FFFFFF",
                fontSize: 16,
                fontWeight: "100",
              },
            },
            {
              text: pie_data.value + "%",
              x: "center",
              y: "center",
              textStyle: {
                fontSize: "60",
                color: "#FFFFFF",
                fontFamily: "DINAlternate-Bold, DINAlternate",
                foontWeight: "600",
              },
            },
          ],
          backgroundColor: "#111",
          polar: {
            radius: ["42%", "52%"],
            center: ["50%", "50%"],
          },
          angleAxis: {
            max: 100,
            show: false,
          },
          radiusAxis: {
            type: "category",
            show: true,
            axisLabel: {
              show: false,
            },
            axisLine: {
              show: false,
            },
            axisTick: {
              show: false,
            },
          },
          series: [
            {
              name: "",
              type: "bar",
              roundCap: true,
              barWidth: 30,
              showBackground: true,
              backgroundStyle: {
                color: "rgba(66, 66, 66, .3)",
              },
              data: [pie_data.value],
              coordinateSystem: "polar",
              itemStyle: {
                normal: {
                  color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                    {
                      offset: 0,
                      color: "#16CEB9",
                    },
                    {
                      offset: 1,
                      color: "#6648FF",
                    },
                  ]),
                },
              },
            },
            {
              name: "",
              type: "pie",
              startAngle: 80,
              radius: ["56%"],
              hoverAnimation: false,
              center: ["50%", "50%"],
              itemStyle: {
                color: "rgba(66, 66, 66, .1)",
                borderWidth: 1,
                borderColor: "#5269EE",
              },
              data: [100],
            },
            {
              name: "",
              type: "pie",
              startAngle: 80,
              radius: ["38%"],
              hoverAnimation: false,
              center: ["50%", "50%"],
              itemStyle: {
                color: "rgba(66, 66, 66, .1)",
                borderWidth: 1,
                borderColor: "#5269EE",
              },
              data: [100],
            },
          ],
        },
        true
      );
    };

    watchEffect(async () => {
      const response = await props.pieData;
      pie_data.value = await response;
      draw();
    });


    return {
      chartDom,
      pie_data,
    };
  },
};
</script>
