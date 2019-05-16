import Vue from 'vue';
import Vuex from 'vuex';
import addresses from './addresses';
import users from './users';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    users,
    addresses,
  },
});
