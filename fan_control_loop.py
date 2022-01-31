import os,sensors,time

# Configurable temperature and fan speed steps
tempSteps = [40, 45, 50, 55, 60, 70]  # [°C]
speedSteps = [5, 10, 15, 20, 35, 50]  # [%]

ipmi_command = "ipmitool raw 0x30 0x30 0x02 0xff"


def get_fanspeed(temperature):
    fanspeed = speedSteps[len(speedSteps) - 1]

    # Below first value, fan will run at min speed.
    if temperature < tempSteps[0]:
        fanspeed = speedSteps[0]
    # Above last value, fan will run at max speed
    elif temperature >= tempSteps[len(tempSteps) - 1]:
        fanspeed = speedSteps[len(tempSteps) - 1]
    # If temperature is between 2 steps, fan speed is calculated by linear interpolation
    else:
        for i in range(0, len(tempSteps) - 1):
            if (temperature >= tempSteps[i]) and (temperature < tempSteps[i + 1]):
                fanspeed = round((speedSteps[i + 1] - speedSteps[i])
                                 / (tempSteps[i + 1] - tempSteps[i])
                                 * (temperature - tempSteps[i])
                                 + speedSteps[i], 1)

    return fanspeed


def main():

    sensors.init()
    try:
        while 1:
            time.sleep(5)
            for chip in sensors.iter_detected_chips():
                # We only care about the coretemp
                if str(chip).startswith("coretemp-"):
                    for feature in chip:
                        # We only care about the package temperature
                        if str(feature.label).startswith("Package id"):
                            os.system("%s 0x%X" % (ipmi_command, int(get_fanspeed(feature.get_value()))))
    finally:
        sensors.cleanup()


if __name__ == '__main__':
    main()
