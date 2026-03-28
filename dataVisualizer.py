import numpy
from matplotlib import animation, pyplot as plot


def main():
    accelerationFile = open("./data/testing/acceleration.txt")
    time_stamp:list[float] = []
    accel_X:list[float] = []
    accel_Y:list[float] = []
    accel_Z:list[float] = []

    for line in accelerationFile:
        splitLine = line.split(",")
        #milliseconds to seconds
        time_stamp.append(float(splitLine[0]) / 1000)
        accel_X.append(float(splitLine[1][1:-1]))
        accel_Y.append(float(splitLine[2][1:-1]))
        accel_Z.append(float(splitLine[3][1:-1]))

    accelerationFile.close()

    

def visualizeAcceleration(accel_X:list[float], accel_Y:list[float], accel_Z:list[float]) -> None:
    #creation of image
    figure = plot.figure()
    axis = figure.add_subplot(projection="3d")

    #set axis
    axis.set_title("Acceleration")
    axis.set(xlim3d= (min(accel_X), max(accel_X)), xlabel = "X")
    axis.set(ylim3d= (min(accel_Y), max(accel_Y)), ylabel = "Y")
    axis.set(zlim3d= (min(accel_Z), max(accel_Z)), zlabel = "Z")

    axis.plot3D(accel_X, accel_Y, accel_Z, zdir="Y")

    plot.savefig("./media/testAcceleration.png")

    plot.show()

def intergrate(time_stamp:list[float], values:list[float]) -> list[float]:
    timeLast:float = time_stamp[0]
    updatedValues:list[float] = []
    for t in range(1, len(time_stamp)):
        deltaTime = time_stamp[t] - timeLast
        updatedValues.append(deltaTime * values[t-1])
        timeLast = time_stamp[t]

    return updatedValues

if (__name__ == "__main__"):
    main()