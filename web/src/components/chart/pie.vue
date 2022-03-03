<!--
 * @Author: wanqqq29
 * @Date: 2022-03-02 10:56:21
 * @LastEditTime: 2022-03-02 10:56:22
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\components\charts\pie.vue
-->
option = {
    title: [
        {
            text: '已完成',
            x: 'center',
            top: '55%',
            textStyle: {
                color: '#FFFFFF',
                fontSize: 16,
                fontWeight: '100',
            },
        },
        {
            text: '75%',
            x: 'center',
            y: 'center',
            textStyle: {
                fontSize: '60',
                color: '#FFFFFF',
                fontFamily: 'DINAlternate-Bold, DINAlternate',
                foontWeight: '600',
            },
        },
    ],
    backgroundColor: '#111',
    polar: {
        radius: ['42%', '52%'],
        center: ['50%', '50%'],
    },
    angleAxis: {
        max: 100,
        show: false,
    },
    radiusAxis: {
        type: 'category',
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
            name: '',
            type: 'bar',
            roundCap: true,
            barWidth: 30,
            showBackground: true,
            backgroundStyle: {
                color: 'rgba(66, 66, 66, .3)',
            },
            data: [60],
            coordinateSystem: 'polar',
            itemStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                        {
                            offset: 0,
                            color: '#16CEB9',
                        },
                        {
                            offset: 1,
                            color: '#6648FF',
                        },
                    ]),
                },
            },
        },
        {
            name: '',
            type: 'pie',
            startAngle: 80,
            radius: ['56%'],
            hoverAnimation: false,
            center: ['50%', '50%'],
            itemStyle: {
                color: 'rgba(66, 66, 66, .1)',
                borderWidth: 1,
                borderColor: '#5269EE',
            },
            data: [100],
        },
        {
            name: '',
            type: 'pie',
            startAngle: 80,
            radius: ['38%'],
            hoverAnimation: false,
            center: ['50%', '50%'],
            itemStyle: {
                color: 'rgba(66, 66, 66, .1)',
                borderWidth: 1,
                borderColor: '#5269EE',
            },
            data: [100],
        },
    ],
};
