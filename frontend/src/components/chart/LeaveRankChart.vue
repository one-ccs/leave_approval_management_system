<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { use } from 'echarts/core';
import { BarChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent, GridComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';
import { type ResponseData } from '@/utils/interface';
import { apiChartLeaveRank } from '@/utils/api';
import DurationRadio from '@/components/DurationRadio.vue';


use([ TitleComponent, TooltipComponent, LegendComponent, GridComponent, BarChart, CanvasRenderer, ]);

const props = withDefaults(defineProps<{
    isVerticalTitle?: boolean;
}>(), {
    isVerticalTitle: false,
});

const option = reactive({
    title: {
        text: props.isVerticalTitle ? '请\n假\n次\n数\n排\n行' : '请假次数排行',
        y: props.isVerticalTitle ? 'middle' : 'auto',
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
        left: props.isVerticalTitle ? '8%' : '3%',
        right: '3%',
        bottom: '12%',
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
                show: true,
            },
            emphasis: {
                focus: 'series',
            },
            data: [3, 1, 0, 1]
        },
        {
            name: '病假',
            type: 'bar',
            stack: 'total',
            label: {
                show: true,
            },
            emphasis: {
                focus: 'series',
            },
            data: [0, 1, 2, 0]
        },
        {
            name: '公假',
            type: 'bar',
            stack: 'total',
            label: {
                show: true,
            },
            emphasis: {
                focus: 'series',
            },
            data: [1, 1, 0, 1]
        },
        {
            name: '出校申请',
            type: 'bar',
            stack: 'total',
            label: {
                show: true,
            },
            emphasis: {
                focus: 'series',
            },
            data: [3, 2, 1, 0]
        },
    ],
});
const duration = ref(90);

const onDurationChange = () => {
    getData();
};

const getData = () => {
    apiChartLeaveRank(duration.value, (data: ResponseData) => {
        option.yAxis.data.length = 0;
        option.series.forEach(item => item.data.length = 0);

        data.data.forEach((item: { userId: number, name: string, total: number, categoryCount: number[] }) => {
            option.yAxis.data.push(item.name);

            option.series[0].data.push(item.categoryCount[0]);
            option.series[1].data.push(item.categoryCount[1]);
            option.series[2].data.push(item.categoryCount[2]);
            option.series[3].data.push(item.categoryCount[3]);
        });
    });
};

onMounted(() => {
    getData();
});
</script>

<template>
    <div class="leave-rank-chart">
        <duration-radio v-model="duration" @change="onDurationChange()" direction="horizontal" />
        <v-chart :option="option" autoresize />
    </div>
</template>

<style scoped lang="less">
</style>
