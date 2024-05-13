<script setup lang="ts">
import LeaveStateChart from '@/components/chart/LeaveStateChart.vue';
import LeaveCountChart from '@/components/chart/LeaveCountChart.vue';
import LeaveRankChart from '@/components/chart/LeaveRankChart.vue';
</script>

<template>
    <div class="portrait">
        <leave-state-chart />
        <leave-count-chart />
        <leave-rank-chart />
    </div>
</template>

<style scoped lang="less">
.portrait {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    padding: var(--padding);

    .chart {
        box-sizing: border-box;
        margin-bottom: 15PX;
        border-radius: var(--border-radius);
        padding: var(--padding);
        background-color: #fff;
        box-shadow: var(--box-shadow-light);

        &:last-child {
            margin-bottom: 0;
        }
        &:nth-child(1) {
            height: 100%;
        }
        &:nth-child(2) {
            height: 100%;
        }
        &:nth-child(3) {
            height: 150%;
        }
    }
}
</style>
