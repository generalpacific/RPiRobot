# Notes for setting up and using inky display

## Setup

Pimoroni provides a python library to control the display.

* Git repo: https://github.com/pimoroni/inky

* Examples: https://github.com/pimoroni/inky/tree/main/examples/7color

* Installing inky:

```
curl https://get.pimoroni.com/inky | bash

```

### Systemd commands

* Copy service to location
```
sudo cp paciframe.service /etc/systemd/system/
```

* Change file permissions
```
sudo chmod 644 /etc/systemd/system/paciframe.service
```

* Enable service
```
sudo systemctl daemon-reload
sudo systemctl enable paciframe.service
```

* Start service
```
sudo systemctl start paciframe.service
```

* Check if the service is active
```
sudo systemctl status paciframe.service
```

* Check if a service is enabled
```
sudo systemctl is-enabled paciframe.service
```
