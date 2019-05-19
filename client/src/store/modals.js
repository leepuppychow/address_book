const modals = {
  namespaced: true,
  state: {
    contactFormVisible: false,
    contactFormType: '',
  },
  getters: {

  },
  mutations: {
    showContactFormPopup(state, formType) {
      state.contactFormVisible = true;
      state.contactFormType = formType;
    },
    hideContactFormPopup(state) {
      state.contactFormVisible = false;
      state.contactFormType = '';
    },
  },
  actions: {
    showContactFormPopup({ commit }, formType) {
      commit('showContactFormPopup', formType);
    },
    hideContactFormPopup({ commit, dispatch }) {
      commit('hideContactFormPopup');
      dispatch('addresses/resetMessages', null, { root: true });
    },
  },
};

export default modals;
