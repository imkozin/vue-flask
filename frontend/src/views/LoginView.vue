<template>
  <div class="container">
      <b-form @submit.prevent="submitLogin" v-if="show" class="custom-border p-3 mt-5">
        <h1 class="text-center">Login</h1>
      <b-form-group id="input-group-1" label="Login:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.login"
          type="text"
          placeholder="Enter login"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          type="password"
          placeholder="Enter password"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="success" class="mt-3">Login</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        login: '',
        password: '',
      },
      show: true,

    };
  },
  methods: {
    async submitLogin() {
    
        try {
            const response = await axios.post('http://localhost:8000/login', this.form);
            if (response.status === 200) {
                const { access_token, user_type } = response.data;
                localStorage.setItem('authData', JSON.stringify({ type: user_type,token: access_token }));
                const data = await response.data;
                console.log(data);
                this.$router.push('/users');
            } else {
                this.errors.push('Invalid credentials');
                // this.snackbar = true
                // this.callSnackbar()
            }
        } catch (err) {
            console.log(err);
            this.errors.push(err.response.data.msg);
            // this.snackbar = true
            // this.callSnackbar()
        }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.custom-border {
  border: 2px solid #42b983;
  border-radius: 5px;
}
</style>
