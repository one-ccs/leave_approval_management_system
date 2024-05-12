<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { use } from 'echarts/core';
import { PieChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';
import { ELeaveState, type ResponseData } from '@/utils/interface';
import { apiChartLeaveState } from '@/utils/api';
import i18n from '@/utils/i18n';


use([ CanvasRenderer, PieChart, TitleComponent, TooltipComponent, ]);

const chartRef = ref();
const option = reactive({
    title: {
        text: '请假状态统计',
    },
    tooltip: {
        trigger: 'item',
    },
    series: [
        {
            name: '请假状态',
            type: 'pie',
            radius: [20, 60],
            center: ['50%', '60%'],
            data: [
                { value: 0, name: '待审批' },
                { value: 0, name: '二审中' },
                { value: 0, name: '已驳回' },
                { value: 0, name: '待销假' },
                { value: 0, name: '销假中' },
                { value: 0, name: '已完成' },
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                },
            },
            label: {
                alignTo: 'labelLine',
                formatter: '{name|{b}}\n{time|{c} 条}',
                minMargin: 5,
                edgeDistance: 10,
                lineHeight: 15,
                rich: {
                    time: {
                        fontSize: 10,
                        color: '#999',
                    },
                },
            },
            labelLine: {
                length: 15,
                length2: 0,
                maxSurfaceAngle: 80,
            },
            labelLayout: function (params: any) {
                const isLeft = params.labelRect.x < chartRef.value.getWidth() / 2;
                const points = params.labelLinePoints;

                points[2][0] = isLeft
                    ? params.labelRect.x
                    : params.labelRect.x + params.labelRect.width;
                return {
                    labelLinePoints: points,
                };
            },
        },
    ],
});

onMounted(() => {
    // 轮流高亮扇形
    let currentIndex = -1;
    let hover = false;
    (chartRef.value.$el as HTMLElement).addEventListener('mouseover', () => {
        hover = true;
        // 取消之前高亮的图形
        chartRef.value.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    });
    (chartRef.value.$el as HTMLElement).addEventListener('mouseleave', () => hover = false);
    setInterval(() => {
        if (hover) return;
        var dataLen = option.series[0].data.length;

        // 取消之前高亮的图形
        chartRef.value.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
        currentIndex = (currentIndex + 1) % dataLen;
        // 高亮当前图形
        chartRef.value.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
        // 显示 tooltip
        chartRef.value.dispatchAction({
            type: 'showTip',
            seriesIndex: 0,
            dataIndex: currentIndex,
        });
    }, 1000);

    apiChartLeaveState((data: ResponseData) => {
        option.series[0].data.length = 0;

        data.data.forEach((item: { state: number, count: number }) => {
            if (item.state === ELeaveState.WITHDRAWN) return;

            option.series[0].data.push({
                value: item.count,
                name: i18n(item.state, 'field.leave.state'),
            });
        });
    });
});
</script>

<template>
    <div class="chart leave-state-chart">
        <v-chart
            class="chart"
            ref="chartRef"
            autoresize
            :option="option"
        />
    </div>
</template>

<style scoped lang="less">
</style>
