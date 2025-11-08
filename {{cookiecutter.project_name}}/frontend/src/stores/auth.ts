import { defineStore } from "pinia";

interface AuthState {
  user: string | null;
  token: string | null;
  isLoggedIn: boolean;
}

export const useAuthStore = defineStore("auth", {
  state: (): AuthState => ({
    user: null,
    token: null,
    isLoggedIn: false,
  }),
  actions: {
    async login(username: string, password: string) {
      const response = await fetch("/api/login/", {
        method: "POST",
        headers: {
          Authorization: "Basic " + btoa(`${username}:${password}`),
          "Content-Type": "application/json",
        },
      });
      if (response.ok) {
        const data = await response.json();
        this.token = data.token;
        this.user = username;
        this.isLoggedIn = true;
        return true;
      }
      return false;
    },
    logout() {
      this.user = null;
      this.token = null;
      this.isLoggedIn = false;
    },
  },
});
