module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // Your Flask backend address
        changeOrigin: true,
        pathRewrite: { '^/api': '' }, // Remove /api prefix when forwarding to Flask
      }
    }
  }
};
