<template>
  <div id="nav" v-if="showHeader">
    <div id="logo-wrapper">
      <img class='address-book-icon' src='../images/address-book-icon.png'/>
      <h2>Addr Reader</h2>
    </div>
    <a @click="logout">LOGOUT</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showHeader: false,
    }
  },
  watch: {
    $route () {
      this.showHeader = this.$route.path === "/" ? false : true;
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('users/logout');
      this.$router.push('/');
    },
  }
}
</script>

<style lang="scss" scoped>
#nav {
  padding: 0;
  margin: 0;
  background: $app-blue;
  height: 60px;
  width: 100vw;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  color: white;

  a {
    font-weight: bold;
    margin-right: 20px;
    cursor: pointer;
  }
  h2 {
    margin-left: 5px;
  }

  #logo-wrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .address-book-icon {
    height: 30px;
    margin-left: 10px;
  }
}
</style>
