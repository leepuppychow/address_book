<template>
  <div>
    <p v-for="a in addresses" :key="a.id">{{ a.street }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    validToken() {
      return this.$store.state.users.success;
    },
    addresses() {
      return this.$store.state.addresses.all;
    }
  },
  beforeRouteEnter(to, from, next) {
    const token = sessionStorage.getItem('addressToken');
    if (!token) next(false);
    next(async (vm) => {
      await vm.$store.dispatch('users/validateToken', token);
      if (!vm.validToken) next('/');
    })
  },
  async created() {
    await this.$store.dispatch('addresses/getAllAddresses');
  }
}
</script>

<style>

</style>

