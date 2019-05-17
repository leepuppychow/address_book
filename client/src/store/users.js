import { login, register } from '../api/api';

const users = {
  namespaced: true,
  state: {
    currentUser: null,
    loading: false,
    error: null,
  },
  getters: {

  },
  mutations: {
    setLoadingStatus(state, status) {
      state.loading = status;
    },
    setError(state, err) {
      state.error = err;
    },
  },
  actions: {
    async login({ commit }, body) {
      try {
        commit('setLoadingStatus', true);
        const response = await login(body);
        const data = await response.json();
        const { token } = data;
        sessionStorage.setItem('addressToken', token);
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', err);
      }
    },
    async register({ commit }, body) {
      try {
        commit('setLoadingStatus', true);
        const response = await register(body);
        const data = await response.json();
        const { token } = data;
        sessionStorage.setItem('addressToken', token);
        commit('setLoadingStatus', false);
      } catch (err) {
        commit('setError', err);
      }
    },
    logout() {
      sessionStorage.removeItem('addressToken');
    },
  },
};

export default users;
