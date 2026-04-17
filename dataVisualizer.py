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

    velocity_X:list[float] = intergrateVelocity(time_stamp, accel_X)
    velocity_Y:list[float] = intergrateVelocity(time_stamp, accel_Y)
    velocity_Z:list[float] = intergrateVelocity(time_stamp, accel_Z)

    position_X:list[float] = intergratePosition(time_stamp, accel_X, velocity_X)
    position_Y:list[float] = intergratePosition(time_stamp, accel_Y, velocity_Y)
    position_Z:list[float] = intergratePosition(time_stamp, accel_Z, velocity_Z)

    visualizeData(accel_X, accel_Y, accel_Z, "Acceleration")
    visualizeData(velocity_X, velocity_Y, velocity_Z, "Velocity")
    visualizeData(position_X, position_Y, position_Z, "Position")

    

def visualizeData(data_X:list[float], data_Y:list[float], data_Z:list[float], name:str) -> None:
    #creation of image
    figure = plot.figure()
    axis = figure.add_subplot(projection="3d")

    #set axis
    axis.set_title(f"{name}")
    axis.set(xlim3d= (min(data_X), max(data_X)), xlabel = "X")
    axis.set(ylim3d= (min(data_Y), max(data_Y)), ylabel = "Y")
    axis.set(zlim3d= (min(data_Z), max(data_Z)), zlabel = "Z")

    axis.plot3D(data_X, data_Y, data_Z)

    plot.savefig(f"./media/test{name}.png")

    plot.show()

#v_f = v_i + (a * t)
def intergrateVelocity(time_stamp:list[float], values:list[float]) -> list[float]:
    timeLast:float = time_stamp[0]
    velocityLast:float = 0
    updatedValues:list[float] = []
    for t in range(1, len(time_stamp)):
        deltaTime = time_stamp[t] - timeLast
        velocityLast += deltaTime * values[t]
        updatedValues.append(velocityLast)
        timeLast = time_stamp[t]

    return updatedValues

#delta x = (v_i * t) + (0.5 * a * t^2)
def intergratePosition(time_stamp:list[float], acceleration:list[float], velocity:list[float]) -> list[float]:
    timeLast:float = time_stamp[0]
    
    newPositions:list[float] = []
    for t in range(1, len(time_stamp)):
        deltaTime = time_stamp[t] - timeLast
        newPositions.append((velocity[t-1] * timeLast) + (0.5 * acceleration[t-1] * (deltaTime * deltaTime)))
        timeLast = time_stamp[t]

    return newPositions

if (__name__ == "__main__"):
    main()