<template>
  <div id="all-contacts">
    <h3>All Contacts</h3>
    <div class="contact-row">
      <p 
        :key="a.id"
        v-for="a in addresses"
        @click="selectContact(a.id)"
      >
        {{ a.first_name }} {{ a.last_name }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    addresses() {
      return this.$store.state.addresses.all;
    }
  },
  methods: {
    selectContact(addressId) {
      debugger
    },
  },
}
</script>

<style lang="scss" scoped>
#all-contacts {
  height: 100%;
  width: 50%;
  border: solid 1px black;
}

</style>
