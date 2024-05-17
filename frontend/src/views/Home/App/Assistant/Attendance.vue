<script setup lang="ts">
import { ref } from 'vue';
import BackNavBar from '@/components/BackNavBar.vue';
import LeaveStateChart from '@/components/chart/LeaveStateChart.vue';
import LeaveCountChart from '@/components/chart/LeaveCountChart.vue';
import LeaveRankChart from '@/components/chart/LeaveRankChart.vue';

const isLandscape = ref(innerWidth > innerHeight);

window.addEventListener('resize', () => {
    isLandscape.value = innerWidth > innerHeight;
});
</script>

<template>
    <div class="view" :class="{ 'landscape': isLandscape }">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <div class="charts">
                <leave-state-chart class="chart" :is-vertical-title="true" />
                <leave-count-chart class="chart" :is-vertical-title="isLandscape" />
                <leave-rank-chart class="chart" :is-vertical-title="isLandscape" />
            </div>
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        padding: var(--padding);

        .charts {
            display: grid;
            grid-template-columns: 1fr;
            grid-template-rows: repeat(2, 1fr) 1.5fr;
            grid-column-gap: var(--padding);
            grid-row-gap: var(--padding);
            width: 100%;
            height: 100%;

            .chart {
                border-radius: var(--border-radius);
                padding: var(--padding);
                background-color: #fff;
                box-shadow: var(--box-shadow-light);
            }
        }
    }
    &.landscape {
        position: fixed;
        width: 100vw;

        .view-container {
            .charts {
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(2, 1fr);
                column-gap: calc(var(--padding) * .65);
                row-gap: calc(var(--padding) * .65);

                .chart {
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
        }
    }
}
</style>
