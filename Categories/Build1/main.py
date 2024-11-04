# gps module implementation
#  captures GPS data (latitude, longitude, speed) to monitor the motorcycle's position and speed.
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

TinyGPSPlus gps;
SoftwareSerial gpsSerial(4, 3);  // RX, TX pins for GPS module

void setup() {
  Serial.begin(9600);         // Serial communication for data output
  gpsSerial.begin(9600);      // Start GPS serial at 9600 baud rate
}

void loop() {
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());

    if (gps.location.isUpdated()) {
      float latitude = gps.location.lat();
      float longitude = gps.location.lng();
      float speed = gps.speed.kmph();

      Serial.print("Latitude: "); Serial.println(latitude);
      Serial.print("Longitude: "); Serial.println(longitude);
      Serial.print("Speed (km/h): "); Serial.println(speed);

      // Check for speeding violation (example: 60 km/h limit)
      if (speed > 60) {
        Serial.println("Speed Violation!");
        // Log violation, e.g., save to SD card or alert system
      }
    }
  }
}
