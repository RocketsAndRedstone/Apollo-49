from matplotlib import animation, pyplot as plot
from math import tan, atan, tau

GRAVITY = -9.81

def main():
    #Open files
    gyroscopeFile = open("./data/testing/gyroscope.txt")
    accelerationFile = open("./data/testing/acceleration.txt")

    timeStamp:list[float] = []
    
    #Yaw, pitch, roll
    gyro_X:list[float] = []
    gyro_Y:list[float] = []
    gyro_Z:list[float] = []

    orientation:list[list[float]] = [[]]
    
    accel_X:list[float] = []
    accel_Y:list[float] = []
    accel_Z:list[float] = []
 
    #Read files and write to lists
    for line in accelerationFile:
        splitLine = line.split(",")
        #milliseconds to seconds
        timeStamp.append(float(splitLine[0]) / 1000)
        accel_X.append(float(splitLine[1]))
        accel_Y.append(float(splitLine[2]))
        accel_Z.append(float(splitLine[3]))

    for line in gyroscopeFile:
        splitLine = line.split(",")
        gyro_X.append(float(splitLine[1]))
        gyro_Y.append(float(splitLine[1]))
        gyro_Z.append(float(splitLine[1]))

    #Close files
    gyroscopeFile.close()
    accelerationFile.close()

    #Inital orientation
    orientation[0].append(atan(GRAVITY / accel_X[0]))
    orientation[0].append(atan(GRAVITY / accel_Y[0]))
    orientation[0].append(atan(GRAVITY / accel_Z[0]))

    orientation = calcOrientation(orientation, gyro_X, gyro_Y, gyro_Z, timeStamp)
    
    accel_X = removeGravity(gyro_X, accel_X, timeStamp)
    accel_Y = removeGravity(gyro_Y, accel_Y, timeStamp)
    accel_Z = removeGravity(gyro_Z, accel_Z, timeStamp)
    #first position only used to determin inital orientation and does not get corrected
    del accel_X[0], accel_Y[0], accel_Z[0], timeStamp[0]

    velocity_X:list[float] = intergrateVelocity(timeStamp, accel_X)
    velocity_Y:list[float] = intergrateVelocity(timeStamp, accel_Y)
    velocity_Z:list[float] = intergrateVelocity(timeStamp, accel_Z)

    position_X:list[float] = intergratePosition(timeStamp, accel_X, velocity_X)
    position_Y:list[float] = intergratePosition(timeStamp, accel_Y, velocity_Y)
    position_Z:list[float] = intergratePosition(timeStamp, accel_Z, velocity_Z)

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
def intergrateVelocity(timeStamp:list[float], values:list[float]) -> list[float]:
    timeLast:float = timeStamp[0]
    velocityLast:float = 0
    updatedValues:list[float] = []
    for t in range(1, len(timeStamp)):
        deltaTime = timeStamp[t] - timeLast
        velocityLast += deltaTime * values[t]
        updatedValues.append(velocityLast)
        timeLast = timeStamp[t]

    return updatedValues

#delta x = (v_i * t) + (0.5 * a * t^2)
def intergratePosition(timeStamp:list[float], acceleration:list[float], velocity:list[float]) -> list[float]:
    timeLast:float = timeStamp[0]
    
    newPositions:list[float] = []
    for t in range(1, len(timeStamp)):
        deltaTime = timeStamp[t] - timeLast
        newPositions.append((velocity[t-1] * timeLast) + (0.5 * acceleration[t-1] * (deltaTime * deltaTime)))
        timeLast = timeStamp[t]

    return newPositions

def removeGravity(gyro:list[float], accel:list[float], timeStamp:list[float]):
    theta:float = atan(GRAVITY / accel[0])
    deltaTime:float = 0
    timeLast:float = timeStamp[0]

    for t in range(1, len(timeStamp)):
        deltaTime = timeStamp[t] - timeLast
        accel[t] = accel[t] - (GRAVITY / tan(theta))
        theta += gyro[t] * deltaTime
        if (theta > tau or theta < -tau):
            theta %= tau
        timeLast = timeStamp[t]    

    return accel

def calcOrientation(initalOrientation:list[list[float]], gyro_X:list[float], gyro_Y:list[float], gyro_Z:list[float], timeStamp:list[float]) -> list[list[float]]:

    orientation:list[list[float]] = [[]]
    deltaTime:float
    timeLast:float = timeStamp[0]

    orientation[0] = initalOrientation[0]

    for t in range(1, len(timeStamp)):
        deltaTime = timeStamp[t] - timeLast
        orientation.append([])
        orientation[t].append(orientation[t - 1][0] + ( gyro_X[t] * deltaTime))
        orientation[t].append(orientation[t - 1][1] + ( gyro_Y[t] * deltaTime))
        orientation[t].append(orientation[t - 1][2] + ( gyro_Z[t] * deltaTime))

        for i in range(3):
            if (orientation[t][i] > tau or orientation[t][i] < -tau):
                orientation[t][i] %= tau

        timeLast = timeStamp[t]

    return orientation

if (__name__ == "__main__"):
    main()