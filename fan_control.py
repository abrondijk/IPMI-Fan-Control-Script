import os

# Configurable temperature and fan speed steps
tempSteps = [30, 40, 50, 60, 70]  # [°C]
speedSteps = [20, 30, 50, 80, 100]  # [%]

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


def get_average_coretemp():
    stream = os.popen('sysctl -a | grep temperature')
    output = stream.read()

    lines = output.split('\n')

    temperatures = []
    for n in range(1, 8):
        # Parse the output per line, split on space and remove final character to only get the temperature, also cast to float
        temperatures.append(float(lines[n].split(' ')[1][:-1]))

    averageTemp = sum(temperatures) / len(temperatures)

    return averageTemp


def main():

    os.system("%s 0x%X" % (ipmi_command, int(get_fanspeed(get_average_coretemp()))))


if __name__ == '__main__':
    main()
