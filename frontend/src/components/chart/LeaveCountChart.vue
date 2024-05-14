<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { use } from 'echarts/core';
import { BarChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';
import { type ResponseData } from '@/utils/interface';
import { apiChartLeaveCount } from '@/utils/api';
import DurationRadio from '@/components/DurationRadio.vue';


use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer]);

const props = withDefaults(defineProps<{
    isVerticalTitle?: boolean;
}>(), {
    isVerticalTitle: false,
});

const option = reactive({
    title: {
        text: props.isVerticalTitle ? '请\n假\n人\n数\n统\n计' : '请假人数统计',
        y: props.isVerticalTitle ? 'middle' : 'auto',
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}<br/>{c}人',
    },
    grid: {
        left: props.isVerticalTitle ? '8%' : '3%',
        top: '25%',
        right: '3%',
        bottom: '15%',
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
const duration = ref(90);

const onDurationChange = () => {
    getData();
};

const getData = () => {
    apiChartLeaveCount(duration.value, (data: ResponseData) => {
        option.xAxis.data.length = 0;
        option.series[0].data.length = 0;

        data.data.forEach((item: { _class: string, leaveCount: { total: number, list: { id: number, name: string, count: number }[] }}) => {
            option.xAxis.data.push(item._class.substring(0, 2) + item._class.substring(item._class.length - 3).replace(' ', ''));
            option.series[0].data.push(item.leaveCount.list.length);
        });
    });
};

onMounted(() => {
    getData();
});
</script>

<template>
    <div class="leave-count-chart">
        <duration-radio v-model="duration" @change="onDurationChange()" direction="horizontal" />
        <v-chart :option="option" autoresize />
    </div>
</template>

<style scoped lang="less">
</style>
