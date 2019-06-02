import Vue from 'vue';
import Vuex from 'vuex';
import addresses from './addresses';
import messages from './messages';
import users from './users';
import modals from './modals';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    users,
    addresses,
    modals,
    messages,
  },
});
