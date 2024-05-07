<script setup lang="ts">
import BackNavBar from '@/components/BackNavBar.vue';
import Portrait from './Attendance/Portrait.vue';
import Landscape from './Attendance/Landscape.vue';
</script>

<template>
    <div class="view">
        <back-nav-bar class="view-header" />
        <div class="view-container">
            <portrait />
            <landscape />
        </div>
    </div>
</template>

<style scoped lang="less">
.view {
    .view-container {
        .portrait {
            display: block;
        }
        .landscape {
            display: none;
        }
    }
}
@media screen and (orientation: landscape) {
    .view {
        position: fixed;
        width: 100vw;

        .view-container {
            .portrait {
                display: none;
            }
            .landscape {
                display: block;
            }
        }
    }
}
</style>
