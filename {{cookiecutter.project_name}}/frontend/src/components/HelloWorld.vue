<template>
  <v-container> Hello world: {{ moves }} </v-container>
</template>

<script setup lang="ts">
import { fetchMoves } from "@/backend/get_django_data";

const moves = ref();

onMounted(async () => {
  const res = await fetchMoves();
  moves.value = res;
});
</script>
