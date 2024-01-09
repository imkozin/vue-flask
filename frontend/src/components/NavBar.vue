<template>
  <nav class="nav">
      <div>
        | <router-link to="/">Home</router-link> |
      </div>
      <div v-if="isAuthenticated">
        <router-link to="/profile">Profile</router-link> |
        <router-link @click="logout" to="/login">Log Out</router-link>
      </div>
      <div v-else>
        <router-link to="/login">Sign In</router-link> |
        <router-link to="/register">Sign Up</router-link>
      </div>
  </nav>
</template>

<script>
import { authMixin } from '@/mixins/authMixin';


export default {
        name: "NavBar",
        mixins: [authMixin],
        methods: {
            logout() {
              this.isAuthenticated = false
              sessionStorage.removeItem('userType')
          },
        },
        mounted() {
          console.log('auth', this.isAuthenticated);
        }
    }
</script>

<style scoped>
.nav {
  display: flex;
  justify-content: space-between;
  background-color: #42b983;
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #06100c;
}
</style>
