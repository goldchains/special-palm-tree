const config = {
    environment: process.env.NODE_ENV || 'dev',
    server: {
      port: process.env.PORT || 4000
    }
  };
  
  module.exports = config;