export const toastMixin = {
  methods: {
    errorMessage(variant = null, error) {
      this.$bvToast.toast(error, {
        title: `Error`,
        variant: variant,
        solid: true,
      })
    },
    authError(variant = null, error) {
      this.$bvToast.toast(error, {
        title: `Authentication Error`,
        variant: variant,
        solid: true,
      })
    },
    successMessage(variant = null, message) {
      this.$bvToast.toast(message, {
        title: `Success`,
        variant: variant,
        solid: true,
      })
    },
  },
}