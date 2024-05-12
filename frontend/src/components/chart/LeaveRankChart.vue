<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { use } from 'echarts/core';
import { BarChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent, GridComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';
import type { ResponseData } from '@/utils/interface';
import { apiChartLeaveRank } from '@/utils/api';


use([ TitleComponent, TooltipComponent, LegendComponent, GridComponent, BarChart, CanvasRenderer, ]);

const option = reactive({
    title: {
        text: '请假次数排行',
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line',
        }
    },
    legend: {
        show: true,
        x: 'center',
        y: 28,
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
    },
    xAxis: {
        type: 'value',
    },
    yAxis: {
        type: 'category',
        inverse: true,
        data: ['张三', '李四', '王五', '赵六'],
    },
    series: [
        {
            name: '事假',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [3, 2, 0, 1]
        },
        {
            name: '病假',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [0, 1, 2, 1]
        },
        {
            name: '公假',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [1, 1, 3, 2]
        },
        {
            name: '出校申请',
            type: 'bar',
            stack: 'total',
            label: {
                show: true
            },
            emphasis: {
                focus: 'series'
            },
            data: [3, 2, 2, 0]
        },
    ],
});

onMounted(() => {
    apiChartLeaveRank((data: ResponseData) => {

        console.log(data);
    });
});
</script>

<template>
    <div class="chart leave-rank-chart">
        <v-chart class="chart" :option="option" autoresize />
    </div>
</template>

<style scoped lang="less">
</style>
