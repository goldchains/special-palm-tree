'use strict';
import * as predictor from '../controllers/predictorController';
import express from 'express';
const router = express.Router();

// predictor Routes
router.route('/:course/:test1')
  .get(predictor.predict_test1);

router.route('/:course/:test1/:test2')
  .get(predictor.predict_test2)
  
export default router;