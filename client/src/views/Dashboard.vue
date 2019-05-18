<template>
  <div id="dashboard">
    <ContactList />
    <ContactCard />
  </div>
</template>

<script>
import ContactList from "../components/ContactList";
import ContactCard from "../components/ContactCard";

export default {
  components: {
    ContactList,
    ContactCard,
  },
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
    await this.$store.dispatch('addresses/getAllContacts');
  }
}
</script>

<style lang="scss" scoped>
#dashboard {
  display: flex;
  flex-flow: row-wrap;
  height: calc(100vh - 60px);
  width: 100vw;
}
</style>

