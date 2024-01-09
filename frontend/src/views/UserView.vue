<template>
    <div class="container-fluid">
        <div v-if="!isAdmin">
    <h2 class="alert alert-info mt-2">User Personal Information</h2>
    <div class="container mt-4">
            <div class="row">
                <div class="col-md-4">
                    <label class="font-weight-bold">First Name:</label>
                    <p>{{ user.fname }}</p>
                </div>
                <div class="col-md-4">
                    <label class="font-weight-bold">Last Name:</label>
                    <p>{{ user.lname }}</p>
                </div>
                <div class="col-md-4">
                    <label class="font-weight-bold">City:</label>
                    <p>{{ user.city }}</p>
                </div>
            </div>

            <div class="row mt-3">
                <div class="col-md-4">
                    <label class="font-weight-bold">Login (Email)</label>
                    <p>{{ user.login }}</p>
                </div>
                <div class="col-md-4">
                    <label class="font-weight-bold">Password</label>
                    <p>{{ '••••••' }}</p>
                </div>
                <div class="col-md-4">
                    <label class="font-weight-bold">Device Quantity:</label>
                    <p>
                        <button class="btn btn-info mr-2" @click="decreaseDeviceQty" :disabled="user.device_qty === 0">-</button>
                        {{ user.device_qty }}
                        <button class="btn btn-primary ml-2" @click="increaseDeviceQty">+</button>
                    </p>

                </div>
            </div>
        </div>
    </div>

        <div v-else class="row mt-3">
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
            </div>

            <div class="col-md-5">
                <div v-if="isEditForm">
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

                <div v-else>
                    <h2 class="alert alert-info">Create A New User</h2>
                    <form @submit.prevent="createUser()">
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
                        <button type="submit" class="btn btn-success float-left ml-2">Save</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {authMixin} from '@/mixins/authMixin';
import { toastMixin } from '@/mixins/toastMixin';
import axios from 'axios';

    export default {
        data() {
            return {
                users: [],
                user: [],
                currentUser: {},
                isEditForm: false,
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
        mixins: [authMixin, toastMixin],
        mounted(){
            console.log('DOM mounted')
            document.title = 'Profile Page'
        },
        beforeMount() {
            this.getUser()
        },
        created() {
            this.getUsers();
        },
        methods: {
            decreaseDeviceQty() {
                this.updateDeviceQty(this.user.device_qty - 1);
            },
            increaseDeviceQty() {
                this.updateDeviceQty(this.user.device_qty + 1);
            },
            async updateDeviceQty(newQty) {
                try {
                    const response = await axios.put(
                    `http://localhost:8000/edit-user-device/${this.user.id}`,
                    { device_qty: newQty },
                    { headers: { 'Content-Type': 'application/json' } } 
                    );
                    this.user.device_qty = newQty;
                    this.getUser();
                    this.successMessage('success', response.data.message);
                } catch (error) {
                    const { data } = error.response;
                    this.errorMessage('danger', data.error);
                    console.error('Error updating user:', error);
                }
            },
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
            async getUser() {
                const authData = JSON.parse(sessionStorage.getItem('authData'))
                const login = authData.login
                try {
                    const response = await axios.get(`http://localhost:8000/get-user/${login}`);
                    const data = response.data;
                    this.user = data.user
                    console.log('user', this.user);
                } catch (error) {
                    console.error('Error fetching users:', error);
                }
            },
            async createUser() {
                try {
                    const response = await axios.post('http://localhost:8000/user/register', this.currentUser, {
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    });
                    const data = response.data;
                    console.log('User registered successfully:', data.message);
                    this.successMessage('success', data.message)
                    this.getUsers();
                    this.isEditForm = false;
                } catch (error) {
                    const { data } = error.response;
                    this.errorMessage('danger', data.error)
                    console.error('Error creating user:', error);
                }
            },
            editBtn(id) {
                const userToEdit = this.users.find((user) => user.id === id);
                    if (userToEdit) {
                        this.currentUser = { ...userToEdit };
                        this.isEditForm = true;
                    }
            },
            async editUser(id) {
                try {
                    const response = await axios.put(`http://localhost:8000/edit-user/${id}`, this.currentUser);
                    this.currentUser = {};
                    this.getUsers();
                    this.successMessage('success', response.data.message)
                    this.isEditForm = false;
                } catch (error) {
                    const { data } = error.response;
                    this.errorMessage('danger', data.error)
                    console.error('Error updating user:', error);
                }
            },
            async deleteUser(id) {
                try {
                    const res = await axios.delete(`http://localhost:8000/delete-user/${id}`);
                    this.getUsers();
                    this.successMessage('success', res.data.message)
                    console.log('User deleted successfully');
                } catch (err) {
                    console.error('Error deleting user:', err.message);
                }
            },
        },
    }
</script>

<style lang="scss" scoped>

</style>