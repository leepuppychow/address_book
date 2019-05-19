module.exports = {
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import "@/styles/colors.scss";
          @import "@/styles/containers.scss";
        `,
      },
    },
  },
};
