export const authMixin = {
//   data() {
//     return {
//       authData: ''
//     }
//   },
  computed: {
    isAdmin() {
      const authDataString = sessionStorage.getItem('authData')
      const authData = JSON.parse(authDataString)
      console.log('data', authData)
      return authData.type === 'admin'
    },
  },
//   methods: {
//     setAuthenticated() {
//       this.isAuthenticated = true
//     },
//   },
}