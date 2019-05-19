import {
  allContacts,
  deleteContact,
  createContact,
  editContact,
} from '../api/api';

const addresses = {
  namespaced: true,
  state: {
    all: [],
    selectedContact: null,
    loading: false,
    error: '',
    successMessage: '',
  },
  getters: {

  },
  mutations: {
    resetState(state) {
      state.all = [];
      state.selectContact = null;
      state.loading = false;
      state.error = '';
      state.successMessage = '';
    },
    resetMessages(state) {
      state.error = '';
      state.successMessage = '';
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
    setSuccessMessage(state, message) {
      state.successMessage = message;
    },
  },
  actions: {
    resetState({ commit }) {
      commit('resetState');
    },
    resetMessages({ commit }) {
      commit('resetMessages');
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
        commit('setError', 'Error getting all contacts');
      }
    },
    async deleteContact({ commit, dispatch }, addressId) {
      try {
        commit('setLoadingStatus', true);
        await deleteContact(addressId);
        dispatch('getAllContacts');
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', 'Error deleting contact');
      }
    },
    async createContact({ commit, dispatch }, payload) {
      try {
        commit('setLoadingStatus', true);
        await createContact(payload);
        dispatch('getAllContacts');
        commit('setLoadingStatus', false);
        commit('setSuccessMessage', 'Contact created successfully!');
      } catch (err) {
        commit('setError', 'Error creating contact');
      }
    },
    async editContact({ commit, dispatch }, payload) {
      try {
        commit('setLoadingStatus', true);
        await editContact(payload.id, payload);
        await dispatch('getAllContacts');
        await dispatch('selectContact', payload.id);
        commit('setLoadingStatus', false);
        commit('setSuccessMessage', 'Contact edited successfully!');
      } catch (err) {
        commit('setError', 'Error editing contact');
      }
    },
  },
};

export default addresses;
