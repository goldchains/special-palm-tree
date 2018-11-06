import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';

import helmet from 'helmet';
import morgan from 'morgan';




import config from './config/config';
import routes from './routes';

const app  = express();


app.use(helmet());
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(morgan('tiny'));

app.use('/', routes);
app.use((req, res, next) => {
  const err = new Error('Not Found');
  err.status = 404;
  next(err);
});
app.use((err, req, res, next) => {
  res.status(err.status || 500);
  res.json({
    error: {
      message: err.message
    }
  });
});

app.listen(config.server.port, () => {
  console.log(`Predictr RESTful API started on: ${config.server.port}`);
});

module.exports = app;