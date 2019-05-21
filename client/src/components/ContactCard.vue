<template>
  <div class="contact-card">
    <div v-if="selectedContact">
      <header>
        <h3>{{ selectedContact.first_name }} {{ selectedContact.last_name }}</h3>
        <button @click="showPopup">Edit Contact</button>
      </header>
      <i class="fas fa-home"></i> 
      <p>{{ selectedContact.street }}</p>
      <p>{{ selectedContact.city }}, {{ selectedContact.state }} {{ selectedContact.zip }}</p>
      <i class="fas fa-phone-volume"></i>
      <p>{{ selectedContact.phone }}</p>
      <i class="far fa-envelope"></i>
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
    border-bottom: 2px solid $app-lightgrey;

    button {
      cursor: pointer;
      border-radius: 5px;
      height: 24px;
      padding: 0 5px;
      background-color: $app-lightgrey;
    }
  }

    height: 45%;
    width: 50%;
    margin: 3% 2% 0 1.5%;
    background-color: $app-white;

    .fa-home, 
    .fa-phone-volume, 
    .fa-envelope {
      font-size: 25px;
      margin-bottom: -10px;
    }

    .fa-home {
      padding-top: 20px;
      color: $app-brown;
    }

    .fa-phone-volume {
      color: $app-blue;
    }

    .fa-envelope {
      color: $app-orange;
    }
}
</style>
