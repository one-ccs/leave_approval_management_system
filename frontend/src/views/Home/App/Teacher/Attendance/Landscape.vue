<script setup lang="ts">
import LeaveStateChart from '@/components/chart/LeaveStateChart.vue';
import LeaveCountChart from '@/components/chart/LeaveCountChart.vue';
import LeaveRankChart from '@/components/chart/LeaveRankChart.vue';
</script>

<template>
    <div class="landscape">
        <leave-state-chart is-vertical-title />
        <leave-count-chart is-vertical-title />
        <leave-rank-chart is-vertical-title />
    </div>
</template>

<style scoped lang="less">
.landscape {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    column-gap: calc(var(--padding) * .65);
    row-gap: calc(var(--padding) * .65);
    padding: var(--padding);
    width: 100%;
    height: 100%;

    .chart {
        border-radius: var(--border-radius);
        padding: var(--padding);
        background-color: #fff;
        box-shadow: var(--box-shadow-light);

        &:last-child {
            margin-bottom: 0;
        }
        &:nth-child(1) {
            grid-area: 1 / 1 / 2 / 2;
        }
        &:nth-child(2) {
            grid-area: 2 / 1 / 3 / 2;
        }
        &:nth-child(3) {
            grid-area: 1 / 2 / 3 / 3;
        }
    }
}
</style>
