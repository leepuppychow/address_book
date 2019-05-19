import {
  allContacts,
  deleteContact,
  createContact,
  editContact,
  zipcodeLookup,
} from '../api/api';

const addresses = {
  namespaced: true,
  state: {
    all: [],
    selectedContact: null,
    loading: false,
    error: '',
    successMessage: '',
    zipcodeLookup: '',
  },
  getters: {

  },
  mutations: {
    resetState(state) {
      state.all = [];
      state.selectedContact = null;
      state.loading = false;
      state.error = '';
      state.successMessage = '';
      state.zipcodeLookup = '';
    },
    resetMessages(state) {
      state.error = '';
      state.successMessage = '';
      state.zipcodeLookup = '';
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
    setZipcodeLookup(state, fullZip) {
      state.zipcodeLookup = fullZip;
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
        commit('setAddresses', response.body);
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', 'Error getting all contacts');
      }
    },
    async deleteContact({ commit, dispatch }, addressId) {
      try {
        commit('setLoadingStatus', true);
        dispatch('resetState');
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
    async zipcodeLookup({ commit }, payload) {
      try {
        commit('setLoadingStatus', true);
        const response = await zipcodeLookup(payload);
        const { zip5, zip4 } = response.body;
        commit('setZipcodeLookup', `${zip5}-${zip4}`);
        commit('setLoadingStatus', false);
        commit('setSuccessMessage', 'Zip code found');
      } catch (err) {
        commit('setError', 'Zip code not found :/');
      }
    },
  },
};

export default addresses;
