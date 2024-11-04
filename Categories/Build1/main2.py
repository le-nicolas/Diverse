#accelerometer and gyroscope
# To detect reckless driving (e.g., sudden braking or acceleration, wheelies), you can use the MPU6050 sensor with an Arduino.
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  if (mpu.testConnection()) {
    Serial.println("MPU6050 connected");
  } else {
    Serial.println("MPU6050 connection failed");
  }
}

void loop() {
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  float accX = ax / 16384.0;
  float accY = ay / 16384.0;
  float accZ = az / 16384.0;

  // Calculate total acceleration for reckless driving detection
  float totalAccel = sqrt(accX * accX + accY * accY + accZ * accZ);

  Serial.print("Acceleration: "); Serial.println(totalAccel);

  if (totalAccel > 2.0) {  // Threshold for detecting sudden movements
    Serial.println("Reckless driving detected!");
    // Log violation or alert rider
  }

  delay(100);
}
