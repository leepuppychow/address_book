<template>
  <div id="dashboard">
    <ContactForm v-if="popupVisible"/>
    <ContactList />
    <ContactCard />
  </div>
</template>

<script>
import ContactList from '../components/ContactList.vue';
import ContactCard from '../components/ContactCard.vue';
import ContactForm from '../components/ContactForm.vue';

export default {
  components: {
    ContactList,
    ContactCard,
    ContactForm,
  },
  computed: {
    popupVisible() {
      return this.$store.state.modals.contactFormVisible;
    },
    validToken() {
      return this.$store.state.users.success;
    },
    addresses() {
      return this.$store.state.addresses.all;
    },
  },
  beforeRouteEnter(to, from, next) {
    const token = sessionStorage.getItem('addressToken');
    if (!token) next(false);
    next(async (vm) => {
      await vm.$store.dispatch('users/validateToken', token);
      if (!vm.validToken) {
        next('/');
      } else {
        await vm.$store.dispatch('addresses/getAllContacts');
        next();
      }
    });
  },
};
</script>

<style lang="scss" scoped>
#dashboard {
  @include flex(row, center, flex-start);
  height: calc(100vh - 60px);
  width: 100vw;
  background-color: $app-lightgrey;
}
</style>
