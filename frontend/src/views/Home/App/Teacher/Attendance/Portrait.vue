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
        margin-bottom: 15px;
        border-radius: var(--border-radius);
        padding: var(--padding);
        height: 100%;
        background-color: #fff;

        &:last-child {
            margin-bottom: 0;
        }
    }
}
</style>
