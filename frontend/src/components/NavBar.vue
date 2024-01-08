<template>
  <nav class="nav">
      <div>
        | <router-link to="/">Home</router-link> |
      </div>
      <div>
        <router-link to="/users">Users</router-link> |
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">Sign Up</router-link>
        <router-link to="/login">Log Out</router-link>
      </div>
  </nav>
</template>


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
