<template>
  <transition name="modal">
    <div class="page-mask">
      <div class="contact-form-modal">
        <header>
          <h3>Contact Form</h3>
          <button @click="closePopup">Close</button>
        </header>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  methods: {
    closePopup() {
      this.$store.dispatch('modals/hideContactFormPopup');
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
  header {
    @include flex(row, space-between, center);
    padding: 0 24px;
    transition: all .3s ease;

    button {
      cursor: pointer;
    }
  }

  width: 70vw;
  height: 80vh;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.3);
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}
</style>
