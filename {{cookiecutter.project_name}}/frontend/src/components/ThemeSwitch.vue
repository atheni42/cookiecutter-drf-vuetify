<template>
  <v-btn icon @click="theme.toggle()">
    <v-icon>{{ icon }}</v-icon>
  </v-btn>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useTheme } from "vuetify";

const theme = useTheme();
const icon = computed(() =>
  theme.name.value === "dark" ? "mdi-weather-night" : "mdi-white-balance-sunny"
);
</script>
