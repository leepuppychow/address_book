<template>
  <div class="login">
    <h1>LOGIN OR REGISTER NOW!</h1>
    <input
      id="login-email"
      type="text"
      placeholder="Enter email"
      v-model="email"
    >
    <input
      id="login-password"
      type="password"
      placeholder="Enter password"
      v-model="password"
    >
    <button id="login" @click="login">Login</button>
    <p>Or</p>
    <button @click="register">Register</button>
    <p id="error-message">{{ userError }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  computed: {
    success() {
      return this.$store.state.users.success;
    },
    userError() {
      return this.$store.state.users.error;
    },
  },
  methods: {
    async login() {
      await this.$store.dispatch('users/login', {
        email: this.email,
        password: this.password,
      });
      if (this.success) this.$router.push('dashboard');
    },
    async register() {
      await this.$store.dispatch('users/register', {
        email: this.email,
        password: this.password,
      });
      if (this.success) this.$router.push('dashboard');
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  @include flex(column, center, center);
  background-image: url('../images/address-book-icon.png');
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  height: 100vh;

  h1, p {
    color: #FFF;
  }
  input {
    width: 400px;
    font-size: 20px;
    padding: 5px;
    margin: 7px;
  }
  button {
    width: 200px;
    height: 32px;
    border-radius: 16px;
    font-size: 20px;
    margin-top: 10px;
    background: #FFF;
  }
  #error-message {
    color: red;
  }
}
</style>
