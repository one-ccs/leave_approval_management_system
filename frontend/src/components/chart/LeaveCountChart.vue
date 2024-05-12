<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { use } from 'echarts/core';
import { BarChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';

import { ELeaveState, type ResponseData } from '@/utils/interface';
import { apiChartLeaveCount } from '@/utils/api';
import { number } from 'echarts';


use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer]);

const option = reactive({
    title: {
        text: '请假人数统计',
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}<br/>{c}人',
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
    },
    xAxis: {
        type: 'category',
        data: ['1班', '2班', '3班', '4班', '5班', '6班', '7班'],
    },
    yAxis: {
        type: 'value',
    },
    series: [
        {
            type: 'bar',
            data: [5, 2, 0, 0, 2, 0, 1],
            label: {
                show: true,
                position: 'top',
                formatter: '{c} 人',
            },
        },
    ],
});

onMounted(() => {
    apiChartLeaveCount((data: ResponseData) => {
        option.xAxis.data.length = 0;
        option.series[0].data.length = 0;

        data.data.forEach((item: { _class: number, count: number}) => {
            option.xAxis.data.push(`${item._class} 班`);
            option.series[0].data.push(item.count);
        });
    });
});
</script>

<template>
    <div class="chart leave-count-chart">
        <v-chart class="chart" :option="option" autoresize />
    </div>
</template>

<style scoped lang="less">
</style>
