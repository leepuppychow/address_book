<template>
  <transition name="modal">
    <div class="page-mask">
      <div class="contact-form-modal">
        <header>
          <h3>{{ headerTitle }}</h3>
          <button @click="closePopup">Close</button>
        </header>
        <div class="form-wrapper">
          <input type="text" placeholder="First Name">
          <input type="text" placeholder="Last Name">
          <input type="text" placeholder="Phone">
          <input type="text" placeholder="Email">
          <input type="text" placeholder="Street">
          <input type="text" placeholder="City">
          <input type="text" placeholder="State">
          <input type="number" placeholder="Zip">
        </div>
        <div>
          <button @click="zipLookup" class="contact-form-btns">Lookup Zipcode</button>
          <button @click="submit" class="contact-form-btns">Submit</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
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
    selectedContact() {
      return this.$store.state.addresses.selectedContact;
    },
  },
  methods: {
    closePopup() {
      this.$store.dispatch('modals/hideContactFormPopup');
    },
    zipLookup() {

    },
    submit() {
      
    },
  },
}
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
  width: 70vw;
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
