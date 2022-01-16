# IPMI-Fan-Control-Script

Needs the ipmitool package installed, as well as the PySensors package.

```
# Run this on startup to enable manual fan control
@reboot /usr/bin/ipmitool raw 0x30 0x30 0x01 0x00
# Need these to run beyond the 1 minute boundary, keep commands in sync.
* * * * *              /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1
* * * * * ( sleep 5  ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 10 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 15 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 20 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 25 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 30 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 35 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 40 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 45 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 50 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
* * * * * ( sleep 55 ; /usr/bin/python3 /path/to/script/fan_control.py >/dev/null 2>&1 )
```
or
```bash
# Run this on startup to enable manual fan control
@reboot /usr/bin/ipmitool raw 0x30 0x30 0x01 0x00

@reboot /usr/bin/python3 /path/to/script/fan_control_loop.py >/dev/null 2>&1
```