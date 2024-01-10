<template>
  <div class="container">
    <h1>Welcome to User State Manager</h1>
    <p>Explore new way of data managing on our website</p>
    <router-link to="/login" class="btn btn-primary">Login</router-link>
  </div>
</template>

<script>
export default {
  mounted() {
    document.title = 'Home Page'
  },
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 50px auto;
  text-align: center;
  height: 70vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btn {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
  text-decoration: none;
  color: #fff;
  background-color: #42b983;
  border-radius: 5px;
  cursor: pointer;
}

.btn:hover {
  background-color: #349d77;
}
</style>
