'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _predictorController = require('../controllers/predictorController');

var predictor = _interopRequireWildcard(_predictorController);

var _express = require('express');

var _express2 = _interopRequireDefault(_express);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }

var router = _express2.default.Router();

// predictor Routes
router.route('/:course/:test1').get(predictor.predict_test1);

router.route('/:course/:test1/:test2').get(predictor.predict_test2);

exports.default = router;