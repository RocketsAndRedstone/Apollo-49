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

    #creation of image
    figure = plot.figure()
    axis = figure.add_subplot(projection="3d")

    #set axis
    axis.set_title("Acceleration")
    axis.set(xlim3d= (min(accel_X), max(accel_X)), xlabel = "X")
    axis.set(ylim3d= (min(accel_Y), max(accel_Y)), ylabel = "Y")
    axis.set(zlim3d= (min(accel_Z), max(accel_Z)), zlabel = "Z")

    axis.plot3D(accel_X, accel_Y, accel_Z, zdir="Y")

    plot.show()

if (__name__ == "__main__"):
    main()