<template>
  <div id="nav" v-if="showHeader">
    <div id="logo-wrapper">
      <img class='address-book-icon' src='../images/owl.png'/>
      <h2>Addr</h2>
    </div>
    <a @click="logout">LOGOUT</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showHeader: false,
    };
  },
  watch: {
    $route() {
      this.showHeader = this.$route.path !== '/';
    },
  },
  methods: {
    async logout() {
      await this.$store.dispatch('users/logout');
      this.$router.push('/');
    },
  },
};
</script>

<style lang="scss" scoped>
#nav {
  @include flex(row, space-between, center);
  padding: 0;
  margin: 0;
  background: $app-blue;
  height: 60px;
  width: 100vw;
  color: white;

  a {
    font-weight: bold;
    margin-right: 20px;
    cursor: pointer;
  }
  h2 {
    margin-left: 5px;
    font-family: 'Trocchi', serif;
    font-size: 24px;
    letter-spacing: 1px;
  }

  #logo-wrapper {
    @include flex(row, center, center);
  }

  .address-book-icon {
    height: 35px;
    margin-left: 10px;
  }
}
</style>
