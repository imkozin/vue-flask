<template>
  <nav class="nav">
      <div>
        | <router-link to="/">Home</router-link> |
      </div>
      <div>
        <router-link to="/profile">Profile</router-link> |
        <a class="link" @click="logout">Log Out</a>
      </div>
      <div>
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
              sessionStorage.removeItem('authData');
              this.$router.push('/login')
          },
        },
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

nav a.router-link-exact-active  {
  color: #06100c;
}

.link {
  color: #06100c;
  cursor: pointer;
}

.link:hover {
  text-decoration: underline;
}
</style>
