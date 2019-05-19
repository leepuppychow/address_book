<template>
  <transition name="modal">
    <div class="page-mask">
      <div class="contact-form-modal">
        <header>
          <h3>{{ headerTitle }}</h3>
          <button @click="closePopup">Close</button>
        </header>
        <div class="form-wrapper">
          <input v-model="firstName" type="text" placeholder="First Name">
          <input v-model="lastName" type="text" placeholder="Last Name">
          <input v-model="phone" type="text" placeholder="Phone">
          <input v-model="email" type="text" placeholder="Email">
          <input v-model="street" type="text" placeholder="Street">
          <input v-model="city" type="text" placeholder="City">
          <input v-model="state" type="text" placeholder="State">
          <input v-model="zip" type="text" placeholder="Zip">
        </div>
        <div>
          <button @click="zipLookup" class="contact-form-btns">Lookup Zipcode</button>
          <button @click="submit" class="contact-form-btns">Submit</button>
        </div>
        <p>{{ message }}</p>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  data() {
    return {
      addressId: 0,
      firstName: '',
      lastName: '',
      phone: '',
      email: '',
      street: '',
      city: '',
      state: '',
      zip: '',
    };
  },
  created() {
    if (this.formType === 'edit' && this.selectedContact) {
      const {
        id, first_name, last_name, phone, email, street, city, state, zip,
      } = this.selectedContact;

      this.addressId = id;
      this.firstName = first_name;
      this.lastName = last_name;
      this.phone = phone;
      this.email = email;
      this.street = street;
      this.city = city;
      this.state = state;
      this.zip = zip;
    }
  },
  computed: {
    formType() {
      return this.$store.state.modals.contactFormType;
    },
    headerTitle() {
      if (this.formType === 'new') {
        return 'Create New Contact';
      } else if (this.formType === 'edit') {
        return 'Edit Contact';
      } else {
        return '';
      }
    },
    message() {
      const { successMessage, error } = this.$store.state.addresses;
      return successMessage || error;
    },
    selectedContact() {
      return this.$store.state.addresses.selectedContact;
    },
  },
  methods: {
    closePopup() {
      this.$store.dispatch('modals/hideContactFormPopup');
    },
    async zipLookup() {
      const payload = {
        street: this.street,
        city: this.city,
        state: this.state,
      };
      await this.$store.dispatch('addresses/zipcodeLookup', payload);
      this.zip = this.$store.state.addresses.zipcodeLookup;
    },
    submit() {
      const payload = {
        id: this.addressId,
        first_name: this.firstName,
        last_name: this.lastName,
        phone: this.phone,
        email: this.email,
        street: this.street,
        city: this.city,
        state: this.state,
        zip: this.zip,
      };

      if (this.formType === 'new') {
        this.$store.dispatch('addresses/createContact', payload);
      } else if (this.formType === 'edit') {
        this.$store.dispatch('addresses/editContact', payload);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.page-mask {
  @include flex(row, center, center);
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  transition: opacity .3s ease;
}

.contact-form-modal {
  width: 50vw;
  height: 80vh;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.3);

  header {
    @include flex(row, space-between, center);
    padding: 0 24px;
    transition: all .3s ease;

    button {
      cursor: pointer;
    }
  }

  .form-wrapper {
    @include flex(column, center, center);

    input {
      font-size: 20px;
      margin: 8px;
    }
  }

  .contact-form-btns {
    cursor: pointer;
    font-size: 16px;
    margin: 20px 4px;
  }
}


.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}
</style>
