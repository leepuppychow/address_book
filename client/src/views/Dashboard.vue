<template>
  
</template>

<script>
export default {
  beforeRouteEnter(to, from, next) {
    const token = sessionStorage.getItem('addressToken');
    if (!token) next(false);
    next(async (vm) => {
      await vm.$store.dispatch('users/validateToken', token);
      if (!vm.validToken) next('/');
    })
  },
  computed: {
    validToken() {
      return this.$store.state.users.success;
    }
  }
}
</script>

<style>

</style>

