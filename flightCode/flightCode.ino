//SD card library imports
#include <SPI.h>
#include <SdFat.h>

// Sensor librarys and declarations
#include "Adafruit_BMP3XX.h"
#include <Adafruit_MPU6050.h>

#define SEALEVELPRESSURE_HPA 1013.25

//7-segment display pins
#define DISPLAY_CLK 5
#define DISPLAY_CS 6
#define DISPLAY_DIN 7

//sensors
Adafruit_BMP3XX barometer;
Adafruit_MPU6050 mpu;

//SD card and files
SdFat sd;
File dataFile, tempFile;
const int SD_PIN = 10;

//display chars + position hex codes
unsigned char hexChars[16]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e};  //common anode '0~F'
unsigned char position[4] = {0x01, 0x02, 0x04, 0x08};

//buttons
const int buttonPin = 2;
const int remoteButonPin = 8;

bool armed = 0;
bool recording = 0;
int remoteState = 0;

//display toggle variables
bool startUp = 0;

void setup() {

  dataFile = sd.open("./launchOne.txt");
  //tempFile = sd.open("./temp.txt");

  //pin initalization for the 7-segment display
  Serial.begin(9600);
  pinMode(DISPLAY_DIN, OUTPUT);
  pinMode(DISPLAY_CLK, OUTPUT);
  pinMode(DISPLAY_CS, OUTPUT);

  //button
  pinMode(buttonPin, INPUT);
  pinMode(remoteButonPin, INPUT);

  barometer.begin_I2C();
  barometer.setPressureOversampling(BMP3_OVERSAMPLING_4X);
  barometer.setTemperatureOversampling(BMP3_OVERSAMPLING_8X);
  barometer.setIIRFilterCoeff(BMP3_IIR_FILTER_COEFF_3);
  barometer.setOutputDataRate(BMP3_ODR_50_HZ);

  mpu.begin();
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_2000_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_260_HZ);
  startUp = 1;
}
void loop() {
  // put your main code here, to run repeatedly:
  if (startUp == 1) {
    sendCmd(hexChars[4], 0x0F);
    delay(250);
  }

  startUp = 0;

  //Arm recording button
  if(digitalRead(buttonPin) == HIGH) {
    armed = !armed;
    delay(250);

    if (armed) {
      sendCmd(hexChars[7], 0x0F);
    }
    else {
      sendCmd(hexChars[9], 0x0F);
    }
    
  }

  remoteState = digitalRead(remoteButonPin);

  //Starts and stops recording with the remote activation button, saves file when clicked agail
  if ((remoteState == HIGH) && armed){
    recording = true;
    sendCmd(hexChars[10], 0x0F);
    delay(250);
  }
  else if (remoteState == LOW && recording && armed){
    recording = false;
    dataFile.close();
    sendCmd(hexChars[12], 0x0F);
    delay(250);
  }

  if (recording){
      sensors_event_t accel, gyro, mpu_temp;
      mpu.getEvent(&accel, &gyro, &mpu_temp);

      float pressure = barometer.pressure / 100.0;
      float baram_temp = barometer.temperature;
      float alt = barometer.readAltitude(SEALEVELPRESSURE_HPA);

      float data[] = {millis(), accel.acceleration.x, accel.acceleration.y, accel.acceleration.z,
      gyro.gyro.x, gyro.gyro.y, gyro.gyro.z, pressure, alt, baram_temp, mpu_temp.temperature};
      for (int i = 0; i < sizeof(data)/sizeof(float); ++i){
        dataFile.println(data[i]);
        Serial.println(data[i]);
      }
      dataFile.println("____________________________________");
      Serial.println("____________________________________");
  }

  delay(50);
}

//From https://easyelecmodule.com/introduction-and-use-of-nixie-tube/
void sendCmd(byte add1, byte dat1) {
  digitalWrite(DISPLAY_CS, LOW);    // Select chip
  //Send data
  for(byte i=0; i<8; i++){
    digitalWrite(DISPLAY_CLK, LOW);
    digitalWrite(DISPLAY_DIN,add1 & 0x80);
    add1 <<= 1;
    digitalWrite(DISPLAY_CLK, HIGH);
  }
  //Send selection signal
  for(byte i=0; i<8; i++){
    digitalWrite(DISPLAY_CLK, LOW);
    digitalWrite(DISPLAY_DIN,dat1 & 0x80);
    dat1 <<= 1;
    digitalWrite(DISPLAY_CLK, HIGH);
  }
  digitalWrite(DISPLAY_CS, HIGH);
}