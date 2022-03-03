<!--
 * @Author: wanqqq29
 * @Date: 2022-03-03 10:36:35
 * @LastEditTime: 2022-03-03 13:03:31
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\charts\wordChart.vue
-->
<template>
  {{ word_data }}
  <div id="word" ref="wordDom" style="height: 300px"></div>
</template>

<script>
import * as echarts from "echarts";
import { onMounted, ref, watchEffect } from "@vue/runtime-core";
import "echarts-wordcloud/dist/echarts-wordcloud.min";

export default {
  props: {
    wordData: Array,
  },
  name: "word",

  setup(props) {
    const word_data = ref("");
    // const word_data = ref("");
    const wordDom = ref(null);
    const draw = () => {
      const wordChart = echarts.init(wordDom.value);
      window.onresize = () => {
        wordChart.resize();
      };
      wordChart.clear();
      wordChart.setOption(
        {
          tooltip: {
            show: false,
          },
          backgroundColor: "#00023f",
          grid: {
            left: 0,
            bottom: 0,
            top: 0,
            right: 0,
          },
          xAxis: {
            type: "category",
            show: false,
          },
          yAxis: {
            max: 100,
            show: false,
          },
          series: [
            {
              type: "wordCloud",
              sizeRange: [8, 60],
              rotationRange: [0, 0],
              textPadding: 100,
              gridSize: 8,
              width: "100%",
              height: "65%",
              left: "center",
              top: "center",
              drawOutOfBound: false,
              textStyle: {
                normal: {
                  color: function () {
                    return (
                      "rgb(" +
                      [
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                        Math.round(Math.random() * 160),
                      ].join(",") +
                      ")"
                    );
                  },
                },
              },
              data: word_data.value,
            },
          ],
        },
        true
      );
    };

    watchEffect(async () => {
      const response = await props.wordData;
      word_data.value = await response;
      setTimeout(()=>{
        draw()
      },500)
    });

    onMounted(() => {});
    return {
      wordDom,
      word_data,
    };
  },
};
</script>
