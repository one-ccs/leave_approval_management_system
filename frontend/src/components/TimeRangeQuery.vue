<script setup lang="ts">
import type { TimeRangePageQuery } from '@/utils/interface';

const model = defineModel({
    type: Object as () => TimeRangePageQuery,
    required: true,
});
const emit = defineEmits<{
    search: [query?: string],
}>();
</script>

<template>
    <div class="time-range-query">
        <van-cell-group>
            <van-field
                v-model="model.query"
                placeholder="请输入要查询的学号、姓名等..."
                autocomplete="off"
                @keypress.enter="$emit('search', model.query)"
            >
                <template #button>
                    <van-button
                        size="small"
                        icon="search"
                        round
                        plain
                        hairline
                        @click="$emit('search', model.query)"
                    ></van-button>
                </template>
            </van-field>
        </van-cell-group>
    </div>
</template>

<style scoped lang="less">
    .time-range-query {
        background-color: #fff;
    }
</style>
