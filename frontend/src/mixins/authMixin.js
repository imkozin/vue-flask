export const authMixin = {
  computed: {
    isAdmin() {
      const authDataString = sessionStorage.getItem('authData')
      const authData = JSON.parse(authDataString)
      console.log('data', authData)
      return authData.type === 'admin'
    },
  },
}