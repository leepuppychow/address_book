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
    padding: 0 24px;

    button {
      cursor: pointer;
    }
  }

  height: 100%;
  width: 50%;
  border: solid 1px $app-blue;
}
</style>
