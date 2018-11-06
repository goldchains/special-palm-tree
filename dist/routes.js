'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _express = require('express');

var _express2 = _interopRequireDefault(_express);

var _predictorRoutes = require('./routes/predictorRoutes');

var _predictorRoutes2 = _interopRequireDefault(_predictorRoutes);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var router = _express2.default.Router();

router.route('/').get(function (req, res) {
  res.json({ message: 'Welcome to the Predictr API!' });
});

router.use('/predict', _predictorRoutes2.default);

exports.default = router;