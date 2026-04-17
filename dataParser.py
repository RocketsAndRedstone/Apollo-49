def main():
    #numDataPoints:int = 0
    masterFile = open("./data/testing/testData.txt")
    accelFile = open("./data/testing/acceleration.txt", "w")
    gyroFile = open("./data/testing/gyroscope.txt", "w")
    barometerFile = open("./data/testing/barometer.txt", "w")
    tempatureFile = open("./data/testing/tempature.txt", "w")

    lineData:float
    lineNumber:int = 0

    
    for line in masterFile:
        lineData = line[:-1]
        match lineNumber:

            case 0:
                accelFile.write(f"{lineData}, ")
                gyroFile.write(f"{lineData}, ")
                barometerFile.write(f"{lineData}, ")
                tempatureFile.write(f"{lineData}, ")
            case 1:
                accelFile.write(f"{lineData}, ")
            case 2:
                accelFile.write(f"{lineData}, ")
            case 3:
                accelFile.write(f"{lineData}")
            case 4:
                gyroFile.write(f"{lineData}, ")
            case 5:
                gyroFile.write(f"{lineData}, ")
            case 6:
                gyroFile.write(f"{lineData}")
            case 7:
                barometerFile.write(f"{lineData}, ")
            case 8:
                barometerFile.write(f"{lineData}")
            case 9:
                tempatureFile.write(f"{lineData}, ")
            case 10:
                tempatureFile.write(f"{lineData}")
            case 11:
                lineNumber = 0
                accelFile.write("\n")
                gyroFile.write("\n")
                barometerFile.write("\n")
                tempatureFile.write("\n")
                continue

        lineNumber += 1


    masterFile.close()
    accelFile.close()
    gyroFile.close()
    barometerFile.close()
    tempatureFile.close()

if (__name__ == "__main__"):
    main()