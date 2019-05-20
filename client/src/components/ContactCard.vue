<template>
  <div class="contact-card">
    <div v-if="selectedContact">
      <header>
        <h3>{{ selectedContact.first_name }} {{ selectedContact.last_name }}</h3>
        <button @click="showPopup">Edit Contact</button>
      </header>
      <p>{{ selectedContact.street }}</p>
      <p>{{ selectedContact.city }}, {{ selectedContact.state }} {{ selectedContact.zip }}</p>
      <p>{{ selectedContact.phone }}</p>
      <p>{{ selectedContact.email }}</p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    selectedContact() {
      return this.$store.state.addresses.selectedContact;
    },
  },
  methods: {
    showPopup() {
      this.$store.dispatch('modals/showContactFormPopup', 'edit');
    },
  },
};
</script>

<style lang="scss" scoped>
.contact-card {
  header {
    @include flex(row, space-between, center);
    padding: 0 15px;

    button {
      cursor: pointer;
      border-radius: 5px;
      height: 24px;
      padding: 0 5px;
      background-color: #f4f2f2;
    }
  }

    height: 30%;
    width: 50%;
    margin: 3% 2% 0 1.5%;
    background-color: #fefefe;
}
</style>
