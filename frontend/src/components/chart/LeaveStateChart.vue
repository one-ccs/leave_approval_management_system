<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue';
import { use } from 'echarts/core';
import { PieChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent } from 'echarts/components';
import { CanvasRenderer } from 'echarts/renderers';
import VChart from 'vue-echarts';
import { type ResponseData } from '@/utils/interface';
import { apiChartLeaveState } from '@/utils/api';
import DurationRadio from '@/components/DurationRadio.vue';


use([ CanvasRenderer, PieChart, TitleComponent, TooltipComponent, ]);

const props = withDefaults(defineProps<{
    isVerticalTitle?: boolean;
}>(), {
    isVerticalTitle: false,
});

const option = reactive({
    title: {
        text: props.isVerticalTitle ? '请\n假\n状\n态\n统\n计' : '请假状态统计',
        y: props.isVerticalTitle ? 'middle' : 'auto',
    },
    tooltip: {
        trigger: 'item',
    },
    series: [
        {
            name: '请假状态',
            type: 'pie',
            radius: ['35%', '75%'],
            center: props.isVerticalTitle ? ['55%', '45%'] : ['50%', '50%'],
            minShowLabelAngle: 9,
            data: [
                { value: 0, name: '待审批' },
                { value: 0, name: '已撤回' },
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
            itemStyle: {
                borderRadius: 8,
                borderColor: '#fff',
                borderWidth: 1,
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
const chartRef = ref();
const duration = ref(90);

const onDurationChange = () => {
    getData();
};

const getData = () => {
    apiChartLeaveState(duration.value, (data: ResponseData) => {
        data.data.forEach((item: { state: number, count: number }) => {
            option.series[0].data[item.state].value = item.count;
        });
    });
};

onMounted(() => {
    getData();

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
});
</script>

<template>
    <div class="leave-state-chart">
        <duration-radio v-model="duration" @change="onDurationChange()" direction="horizontal" />
        <v-chart
            ref="chartRef"
            autoresize
            :option="option"
        />
    </div>
</template>

<style scoped lang="less">
</style>
