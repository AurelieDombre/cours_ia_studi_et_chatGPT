const { getDefaultConfig } = require("expo/metro-config");

const config = getDefaultConfig(__dirname);

config.resolver.assetExts.push("wasm");

const defaultEnhanceMiddleware = config.server.enhanceMiddleware;

config.server.enhanceMiddleware = (middleware, server) => {
  const enhancedMiddleware = defaultEnhanceMiddleware
    ? defaultEnhanceMiddleware(middleware, server)
    : middleware;

  return (req, res, next) => {
    res.setHeader("Cross-Origin-Opener-Policy", "same-origin");
    res.setHeader("Cross-Origin-Embedder-Policy", "require-corp");
    enhancedMiddleware(req, res, next);
  };
};

module.exports = config;
