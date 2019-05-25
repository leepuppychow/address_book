<template>
  <div id="all-contacts">
    <header>
      <h3>ALL CONTACTS</h3>
      <button @click="showPopup">Add Contact</button>
    </header>
    <div
      class="contact-wrapper"
      :key="a.id"
      v-for="a in addresses"
      @click="selectContact(a.id)"
    >
      <p class="contact-row">
        {{ a.first_name }} {{ a.last_name }}
      </p>
      <img
        @click="deleteContact(a.id)"
        class="delete-icon"
        src="@/images/delete.svg"
        alt="delete"
      >
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    addresses() {
      return this.$store.state.addresses.all;
    },
    favorites() {
      return this.$store.getters['addresses/favorites'];
    },
  },
  methods: {
    showPopup() {
      this.$store.dispatch('modals/showContactFormPopup', 'new');
    },
    selectContact(addressId) {
      this.$store.dispatch('addresses/selectContact', addressId);
    },
    deleteContact(addressId) {
      this.$store.dispatch('addresses/deleteContact', addressId);
    },
  },
};
</script>

<style lang="scss" scoped>
#all-contacts {
  height: 98%;
  width: 50%;
  margin: 3% 3% 0 2%;
  background-color: $app-white;

  header {
    @include flex(row, space-between, center);
    padding: 0 15px;
    border-bottom: 2px solid $app-lightgrey;

    button {
      cursor: pointer;
      border-radius: 5px;
      height: 24px;
      padding: 0 5px;
      background-color: $app-lightgrey;
    }
  }
}
.contact-wrapper {
  @include flex(row, space-between, center);
  border-bottom: 2px solid $app-lightgrey;
  cursor: pointer;

  .contact-row {
    white-space: nowrap;
    margin-left: 15px;

    &:hover {
      text-decoration: underline;
      font-weight: 600;
    }
  }
  .delete-icon {
    cursor: pointer;
    height: 20px;
    width: auto;
    margin-right: 15px;
  }
}
</style>
