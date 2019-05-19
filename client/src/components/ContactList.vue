<template>
  <div id="all-contacts">
    <ContactForm v-if="popupVisible"/>
    <header>
      <h3>All Contacts</h3>
      <button @click="showPopup">Add New Contact</button>
    </header>
    <div 
      class="contact-wrapper"
      :key="a.id"
      v-for="a in addresses"
    >
      <p 
        class="contact-row"
        @click="selectContact(a.id)"
      >
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
import ContactForm from './ContactForm';

export default {
  components: {
    ContactForm,
  },
  computed: {
    popupVisible() {
      return this.$store.state.modals.contactFormVisible;
    },
    addresses() {
      return this.$store.state.addresses.all;
    },
  },
  methods: {
    showPopup() {
      this.$store.dispatch('modals/showContactFormPopup');
    },
    selectContact(addressId) {
      this.$store.dispatch('addresses/selectContact', addressId);
    },
    deleteContact(addressId) {
      this.$store.dispatch('addresses/deleteContact', addressId);
    }
  },
}
</script>

<style lang="scss" scoped>
#all-contacts {
  height: 100%;
  width: 50%;
  border: solid 1px $app-blue;

  header {
    @include flex(row, space-between, center);
    padding: 0 24px;

    button {
      cursor: pointer;
    }
  }
}
.contact-wrapper {
  @include flex(row, center, center);

  .contact-row {
    cursor: pointer;
    white-space: nowrap;
  }
  .delete-icon {
    cursor: pointer;
    height: 20px;
    margin-left: 36px;
    width: auto;
  }
}
</style>
