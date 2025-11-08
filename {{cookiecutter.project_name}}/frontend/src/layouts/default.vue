<template>
  <v-layout height="90%">
    <SystemBar />
    <navigation-bar />
    <v-main>
      <router-view />
    </v-main>
  </v-layout>
  <AppFooter />
</template>

<script lang="ts" setup>
import SystemBar from "@/components/layout/SystemBar.vue";
import AppFooter from "@/components/layout/AppFooter.vue";
import NavigationBar from "@/components/layout/NavigationBar.vue";
</script>
