import { login, register, validateToken } from '../api/api';

const users = {
  namespaced: true,
  state: {
    loading: false,
    success: false,
    error: '',
  },
  getters: {

  },
  mutations: {
    setLoadingStatus(state, status) {
      state.loading = status;
    },
    setSuccessStatus(state, status) {
      state.success = status;
    },
    setError(state, err) {
      state.error = err;
    },
    resetState(state) {
      state.loading = false;
      state.success = false;
      state.error = '';
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
        commit('setSuccessStatus', true);
      } catch (_err) {
        commit('setError', 'Error with login, please try again');
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
        commit('setSuccessStatus', true);
      } catch (_err) {
        commit('setError', 'Email already taken, please try again');
      }
    },
    async validateToken({ commit }, authToken) {
      try {
        commit('setLoadingStatus', true);
        await validateToken(authToken);
        commit('setLoadingStatus', false);
        commit('setSuccessStatus', true);
      } catch (_err) {
        commit('setError', ''); // Dont display any feedback to bad actor
      }
    },
    logout({ commit }) {
      sessionStorage.removeItem('addressToken');
      commit('resetState');
    },
    resetState({ commit }) {
      commit('resetState');
    },
  },
};

export default users;
