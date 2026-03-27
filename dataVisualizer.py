import numpy
from matplotlib import animation, pyplot as plot


def main():
    accelerationFile = open("./data/testing/acceleration.txt")
    time_stamp:float = []
    accel_X:float = []
    accel_Y:float = []
    accel_Z:float = []

    for line in accelerationFile:
        splitLine = line.split(",")
        time_stamp.append(float(splitLine[0]))
        accel_X.append(float(splitLine[1][1:-1]))
        accel_Y.append(float(splitLine[2][1:-1]))
        accel_Z.append(float(splitLine[3][1:-1]))

    accelerationFile.close()


if (__name__ == "__main__"):
    main()