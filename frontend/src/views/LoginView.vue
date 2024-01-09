<!-- <template>
  <div class="container">
      <b-form @submit.prevent="submitLogin" v-if="show" class="custom-border p-5 mt-5">
        <h1 class="text-center">Sign In</h1>
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
      <p>Not a member? <router-link to="/register" class="text-success">Sign up here</router-link></p>
      <b-button type="submit" variant="success" class="mt-3">Login</b-button>
    </b-form>
  </div>
</template> -->

<template>
  <div class="container d-flex align-items-center justify-content-center min-vh-90">
    <b-form @submit.prevent="submitLogin" class="custom-border p-5">
      <h1 class="text-center">Sign In</h1>

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

      <p>Not a member? <router-link to="/register" class="text-success">Sign up here</router-link></p>
      
      <b-button type="submit" variant="success" class="mt-3">Login</b-button>
    </b-form>
  </div>
</template>


<script>
import {authMixin} from '@/mixins/authMixin';
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        login: '',
        password: '',
      },
    };
  },
  mounted() {
    document.title = 'Sign In'
  },
  mixins: [authMixin],
  methods: {
    authError(variant = null, error) {
        this.$bvToast.toast(error, {
          title: `Authentication Error`,
          variant: variant,
          solid: true
        })
    },
    async submitLogin() {
        try {
            const response = await axios.post('http://localhost:8000/login', this.form);
            if (response.status === 200) {
                const { access_token, user_type } = response.data;
                sessionStorage.setItem('authData', JSON.stringify({ type: user_type, token: access_token }));
                // this.setAuthenticated();
                this.$router.push('/profile');
            } else {
                this.authError('danger', 'An error occurred');
            }
        } catch (err) {
            console.error(err)
            const { data } = err.response;
            this.authError('danger', data.error);
        }
    }
  },
};
</script>

<style scoped>
.container {
  height: calc(90vh - 60px);
}

.custom-border {
  border: 2px solid #42b983;
  border-radius: 10px;
}
</style>
