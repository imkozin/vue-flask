<template>
    <div class="container-fluid"> 
        <h2 class="alert alert-danger mt-2">User Personal Information</h2>
        <div class="row">
            <div class="col-md-7">
                <h2 class="alert alert-success">List of Users</h2>
                <table class="table table-bordered mt-4">
            <thead>
                <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Login (Email)</th>
                    <th scope="col">Password</th>
                    <th scope="col">City</th>
                    <th scope="col">Device Quantity</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in users">
                <td>{{user.fname}}</td>
                <td>{{user.lname}}</td>
                <td>{{user.login}}</td>
                <td>{{ '••••••' }}</td>
                <td>{{user.city}}</td>
                <td >{{ user.device_qty ? user.device_qty : 0}}</td>
                <td>
                    <a href="#" class="edit" title="" ><button @click="editBtn(user.id)" class="btn btn-success btn-sm">Edit</button></a>
                    <a href="#" class="edit ml-1" title="" ><button @click="deleteUser(user.id)"  class="btn btn-danger btn-sm">Delete</button></a>
                </td>
                </tr>
            </tbody>
            </table>
<div class="col-md-5">
    <div v-if="Object.keys(this.currentUser).length !== 0">
    <h2 class="alert alert-warning">Edit User Details</h2>

    <form @submit.prevent="editUser(currentUser.id)">
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
              <label class="form-label float-left ml-2">Devices</label>
              <input type="text" class="form-control" v-model="currentUser.device_qty">
            </div>
          </div>
        </div>
        <button type="submit" class="btn btn-success float-left ml-2">Update</button>
      </form>
</div>
<!-- 
                <div v-else>
                    <h2 class="alert alert-info">Create A New Student</h2>
                    <form @submit.prevent="saveUser()">

<div class="row">

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Name</label>
<input type="text" class="form-control" v-model="User.name">
</div>
    </div>

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Email</label>
<input type="email" class="form-control" v-model="student.email">
</div>
    </div>
</div>



<div class="row">
<div class="col">
<div class="form-group">
<label class="form-label float-left ml-2">Course</label>
<input type="text" class="form-control" v-model="student.course">
</div>
</div>
<div class="col">

<div class="form-group">
<label class="form-label float-left ml-2">Gender</label>
<input type="text" class="form-control" v-model="student.gender">
</div>
</div>

</div>
<button type="submit" class="btn btn-primary float-left ml-2">Save</button>
</form>
                </div> -->
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        data() {
            return {
                users: [],
                currentUser: {},
                user: {
                    fname: '',
                    lname: '',
                    password: '',
                    login: '',
                    city: '',
                    device_qty: '',
                }
            }
        },
        methods: {
            async getUsers() {
                try {
                    const response = await axios.get('http://localhost:8000/api/users');
                    const data = response.data;
                    this.users = data.users
                    console.log('users', this.users);
                } catch (error) {
                    console.error('Error fetching users:', error);
                }
            },
            editBtn(id) {
                const userToEdit = this.users.find((user) => user.id === id);
                    if (userToEdit) {
                        this.currentUser = { ...userToEdit };
                    }
            },
            async editUser(id) {
                try {
                    const response = await axios.put(`http://localhost:8000/edit-user/${id}`, this.currentUser);
                    console.log('User updated successfully:', response.data);
                    this.currentUser = {};
                    this.getUsers();
                } catch (error) {
                    console.error('Error updating user:', error);
                }
            },
            async deleteUser(id) {
                try {
                    const res = await axios.delete(`http://localhost:8000/delete-user/${id}`);
                    this.getUsers();
                    console.log('User deleted successfully');
                } catch (err) {
                    console.error('Error deleting user:', err.message);
                }
            },
        },
        mounted(){
            console.log('DOM mounted')
            this.getUsers();
        },
        // created() {
        // },
    }
</script>

<style lang="scss" scoped>

</style>