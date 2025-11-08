<template>
  <v-system-bar>Adelaide Time: {{ now }}</v-system-bar>
</template>

<script setup lang="ts">
import { DateTime } from "luxon";
const now = ref(DateTime.now().toLocaleString(DateTime.DATETIME_MED));
</script>
<style></style>
