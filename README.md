# IPMI-Fan-Control-Script

Needs the ipmitool package installed, as well as the PySensors package.

```
# Enable manual fan control
@reboot /usr/bin/ipmitool raw 0x30 0x30 0x01 0x00
# Run fan control
@reboot /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1
```
