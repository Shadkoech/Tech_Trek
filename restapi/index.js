// simple Express.js RESTful API
'use strict';

// initialize
const
  port = 8888;
const express = require('express');
const app = express();

// /hello/ GET request
app.get('/hello/:name?', (req, res) =>
  res.json(
    { message: `Hello ${req.params.name || 'Koech!!'}!` }
  )
);

// start server
app.listen(port, () =>
  console.log(`Server started on port ${port}`)
);
