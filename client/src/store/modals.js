const modals = {
  namespaced: true,
  state: {
    contactFormVisible: false,
  },
  getters: {

  },
  mutations: {
    showContactFormPopup(state) {
      state.contactFormVisible = true;
    },
    hideContactFormPopup(state) {
      state.contactFormVisible = false;
    },
  },
  actions: {
    showContactFormPopup({ commit }) {
      commit('showContactFormPopup');
    },
    hideContactFormPopup({ commit }) {
      commit('hideContactFormPopup');
    },
  },
};

export default modals;
