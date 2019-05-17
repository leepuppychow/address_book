import { 
  allAddresses,
  findAddress,
  deleteAddress,
  createAddress,
  editAddress,
} from '../api/api';

const addresses = {
  namespaced: true,
  state: {
    all: [],
    loading: false,
    error: '',
  },
  getters: {

  },
  mutations: {
    resetState(state) {
      state.all = [];
      state.loading = false;
      state.error = '';
    },
    setLoadingStatus(state, status) {
      state.loading = status;
    },
    setError(state, err) {
      state.error = err;
    },
    setAddresses(state, payload) {
      state.all = payload;
    },
  },
  actions: {
    resetState({ commit }) {
      commit('resetState');
    },
    async getAllAddresses({ commit }) {
      try {
        commit('setLoadingStatus', true);
        const response = await allAddresses();
        const payload = await response.json();
        commit('setAddresses', payload);
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', 'Error getting all addresses');
      }
    },
  },
};

export default addresses;
