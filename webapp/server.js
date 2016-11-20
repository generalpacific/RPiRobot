var express = require('express');
var app = express();

app.get('/index.html', function (req, res) {  
  console.log("Got request: /index.html")
  res.sendFile(__dirname + "/" + "index.html");
});

app.get('/', function (req, res) {  
  console.log("Got request: /")
  res.sendFile(__dirname + "/" + "index.html");
});

var server = app.listen(8081, function() {
  var host = server.address().address
  var port = server.address().port

  console.log("Listening at http://%s:%s", host, port)
})
