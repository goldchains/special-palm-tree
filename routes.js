import express from 'express';
const router = express.Router();

import predictors from './routes/predictorRoutes';

router.route('/').get((req, res) => {
  res.json({ message: 'Welcome to the Predictr API!' });
});

router.use('/predict', predictors);

export default router;