var express = require('express');
var router = express.Router();
var iot = require("../iotpublish")

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Pacific RPi Robot' });
});

router.post('/forward', function(req, res, next) {
  console.log("Forward request: " + req.body)
  iot.publish()
  res.end("Success")
});

module.exports = router;
