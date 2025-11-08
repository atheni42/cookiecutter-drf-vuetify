<template>
  <v-card class="mx-auto my-12" max-width="400">
    <v-card-title v-if="!authStore.isLoggedIn">Login</v-card-title>
    <v-card-title v-else>Username: {{ authStore.user }}</v-card-title>
    <v-card-text>
      <v-form ref="form" @submit.prevent="onSubmit" v-model="valid">
        <div v-if="!authStore.isLoggedIn">
          <v-text-field
            label="Username"
            v-model="username"
            :rules="[rules.required]"
            required
          />
          <v-text-field
            label="Password"
            v-model="password"
            :rules="[rules.required]"
            type="password"
            required
          />
        </div>
        <v-alert v-if="error" type="error">{{ error }}</v-alert>
        <v-row class="mt-4">
          <v-col cols="6">
            <v-btn @click="authStore.logout()" color="error" width="100%">
              Logout
            </v-btn>
          </v-col>
          <v-col cols="6">
            <v-btn type="submit" width="100%"> Login </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

const username = ref("");
const password = ref("");
const error = ref("");
const valid = ref(false);
const form = ref();

const rules = {
  required: (v: string) => !!v || "Required",
};

const onSubmit = async () => {
  error.value = "";
  const success = await authStore.login(username.value, password.value);
  if (success) {
    router.push({ name: "/" });
  } else {
    error.value = "Invalid credentials";
  }
};
</script>

<style scoped>
.v-card {
  padding: 1rem;
}
</style>
