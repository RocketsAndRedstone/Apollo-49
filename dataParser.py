def main():
    #numDataPoints:int = 0
    masterFile = open("testData.txt")
    accelFile = open("acceleration.txt", "w")
    gyroFile = open("gyroscope.txt", "w")
    barometerFile = open("barometer.txt", "w")
    tempatureFile = open("tempature.txt", "w")

    timeStamp:float
    data:float
    dataLine:int = 0

    
    for line in masterFile:
        match dataLine:

            case 0:
                timeStamp = line[:-1]
                accelFile.write(f"{timeStamp}, ")
                gyroFile.write(f"{timeStamp}, ")
                barometerFile.write(f"{timeStamp}, ")
                tempatureFile.write(f"{timeStamp}, ")
            case 1:
                accelFile.write(f"{line[:-1]}; ")
            case 2:
                accelFile.write(f"{line[:-1]}: ")
            case 3:
                accelFile.write(f"{line[:-1]}")
            case 4:
                gyroFile.write(f"{line[:-1]}; ")
            case 5:
                gyroFile.write(f"{line[:-1]}: ")
            case 6:
                gyroFile.write(f"{line[:-1]}")
            case 7:
                barometerFile.write(f"{line[:-1]}; ")
            case 8:
                barometerFile.write(f"{line[:-1]}")
            case 9:
                tempatureFile.write(f"{line[:-1]}; ")
            case 10:
                tempatureFile.write(f"{line[:-1]}")
            case 11:
                dataLine = 0
                accelFile.write("\n")
                gyroFile.write("\n")
                barometerFile.write("\n")
                tempatureFile.write("\n")
                continue

        dataLine += 1


    masterFile.close()
    accelFile.close()
    gyroFile.close()
    barometerFile.close()
    tempatureFile.close()

if (__name__ == "__main__"):
    main()