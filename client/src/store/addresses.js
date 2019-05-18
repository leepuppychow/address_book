import { 
  allContacts,
  deleteContact,
} from '../api/api';

const addresses = {
  namespaced: true,
  state: {
    all: [],
    selectedContact: null,
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
    selectContact(state, addressId) {
      state.selectedContact = state.all.find(a => a.id === addressId);
    },
  },
  actions: {
    resetState({ commit }) {
      commit('resetState');
    },
    selectContact({ commit }, addressId) {
      commit('selectContact', addressId);
    },
    async getAllContacts({ commit }) {
      try {
        commit('setLoadingStatus', true);
        const response = await allContacts();
        const payload = await response.json();
        commit('setAddresses', payload);
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', 'Error getting all addresses');
      }
    },
    async deleteContact({ commit, dispatch }, addressId) {
      try {
        commit('setLoadingStatus', true);
        await deleteContact(addressId);
        debugger;
        dispatch('getAllContacts');
      } catch (err) {
        commit('setError', 'Error deleting address');
      }
    },
  },
};

export default addresses;
