<template>
  <v-app-bar>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>My Stack</v-toolbar-title>
    <theme-switch />
  </v-app-bar>

  <v-navigation-drawer
    v-model="drawer"
    :location="$vuetify.display.mobile ? 'bottom' : undefined"
    temporary
  >
    <v-list>
      <v-list-item
        prepend-icon="mdi-login"
        :title="authStore.isLoggedIn ? authStore.user as string : 'Login'"
        to="/login"
      ></v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list>
      <v-list-item
        link
        prepend-icon="mdi-home"
        title="Home"
        to="/"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import ThemeSwitch from "../ThemeSwitch.vue";
import { useAuthStore } from "@/stores/auth";

const drawer = ref(false);
const group = ref(null);
const authStore = useAuthStore();

watch(group, () => {
  drawer.value = false;
});
</script>
<style></style>
