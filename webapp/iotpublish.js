var awsIot = require('aws-iot-device-sdk');
var fs = require('fs');

// Read config values from a JSON file.
var config = fs.readFileSync('./aws_iot_config.json', 'utf8');
config = JSON.parse(config);

// Initialize device
var device = awsIot.device({
   keyPath: config.KEY_PATH,
  certPath: config.CERT_PATH,
    caPath: config.CA_PATH,
  clientId: config.CLIENT_ID,
    region: config.REGION 
});

device
  .on('connect', function() {
      console.log('AWS IOT Connected');
});

module.exports = {
  publish: function() {
            console.log("Publish")
            device.publish('RPiRobot/sub', "f");
  }
}
