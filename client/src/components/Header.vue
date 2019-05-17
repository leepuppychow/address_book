<template>
  <div id="nav">
    <a v-if="showLogout" @click="logout">LOGOUT</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showLogout: false,
    }
  },
  watch: {
    $route () {
      this.showLogout = this.$route.path === "/" ? false : true;
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
  background: #42b983;
  height: 60px;
  width: 100vw;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;

  a {
    font-weight: bold;
    color: #2c3e50;
    margin-right: 20px;
    cursor: pointer;
  }
}
</style>
