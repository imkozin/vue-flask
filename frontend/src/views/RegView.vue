<template>
  <div class="container d-flex align-items-center justify-content-center min-vh-90">
    <b-form @submit.prevent="submitReg" class="custom-border p-5">
      <h1 class="text-center">Sign Up</h1>

      <div class="row">
        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">First Name</label>
            <input type="text" class="form-control" v-model="currentUser.fname">
          </div>
        </div>

        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">Last Name</label>
            <input type="text" class="form-control" v-model="currentUser.lname">
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">City</label>
            <input type="text" class="form-control" v-model="currentUser.city">
          </div>
        </div>

        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">Login (Email)</label>
            <input type="email" class="form-control" v-model="currentUser.login">
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">Password</label>
            <input type="password" class="form-control" v-model="currentUser.password">
          </div>
        </div>

        <div class="col">
          <div class="form-group">
            <label class="form-label float-left ml-2">Device Qty</label>
            <input type="number" class="form-control" v-model="currentUser.device_qty" min="0">
          </div>
        </div>
      </div>

      <p>Already a member? <router-link to="/login" class="text-success">Sign in here</router-link></p>

      <div class="row">
        <div class="col">
          <button type="submit" class="btn btn-success btn-block">Register</button>
        </div>
      </div>
    </b-form>
  </div>
</template>


<script>
import axios from 'axios';
import { authMixin } from '@/mixins/authMixin';
import {toastMixin} from '@/mixins/toastMixin'

export default {
  data() {
    return {
      currentUser: {
        fname: '',
        lname: '',
        city: '',
        login: '',
        password: '',
        device_qty: 0,
      },
    };
  },
  mixins: [authMixin, toastMixin],
  mounted() {
    document.title = 'Sign Up'
  },
  methods: {
    async submitReg() {
      try {
            const response = await axios.post('https://flask-server-6kzx.onrender.com/api/user/register', this.currentUser, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            this.$router.push('/login');
        } catch (error) {
            const { data } = error.response;
            this.errorMessage('danger', data.error)
            console.error('Error creating user:', error);
        }
    },
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