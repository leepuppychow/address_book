<template>
  <div class="contact-card">
    <div v-if="selectedContact">
      <p>{{ selectedContact.first_name }} {{ selectedContact.last_name }}</p>
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
    }
  },
}
</script>

<style lang="scss" scoped>
.contact-card {
  height: 100%;
  width: 50%;
  border: solid 1px $app-blue;
}

</style>
