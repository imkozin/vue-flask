export const authMixin = {
  computed: {
    isAdmin() {
      const authData = JSON.parse(sessionStorage.getItem('authData'))
      return authData && authData.type === 'admin'
    },
    isAuthenticated() {
      const authData = JSON.parse(sessionStorage.getItem('authData'))
      return authData && authData.token !== ''
    },
  },
}
