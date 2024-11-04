┌────────────────────────────────────────────────────────────────────┐
│                             Motorcycle                              │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │                          Hardware Layer                        │ │
│ │  ┌───────────────┬─────────────┬─────────────┬──────────────┐   │ │
│ │  │    GPS        │ Accelerometer│ Gyroscope   │  Speed Sensor│   │ │
│ │  └───────────────┴─────────────┴─────────────┴──────────────┘   │ │
│ │                  │               │                             │ │
│ │                  ▼               ▼                             │ │
│ │          ┌──────────────────────────────────┐                  │ │
│ │          │          Main Controller          │                  │ │
│ │          │   (Arduino, ESP32, or Raspberry Pi)│                  │ │
│ │          └──────────────────────────────────┘                  │ │
│ │                  │               │                             │ │
│ │                  ▼               ▼                             │ │
│ │        ┌──────────────────────────────────┐                    │ │
│ │        │      Camera (Optional, Triggered) │                    │ │
│ │        └──────────────────────────────────┘                    │ │
│ │                                                                  │ │
│ │        ┌──────────────────────────────────┐                     │ │
│ │        │        SD Card (Local Logging)    │                     │ │
│ │        └──────────────────────────────────┘                     │ │
│ │                                                                  │ │
│ │  ┌───────────────┬─────────────┬─────────────┬──────────────┐     │ │
│ │  │  Wi-Fi Module │  Bluetooth  │ Cellular    │ Power Supply │     │ │
│ │  └───────────────┴─────────────┴─────────────┴──────────────┘     │ │
│ └────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘

 ┌────────────────────────────────────────────────────────────────────┐
 │                        Software Architecture                        │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │   1. Data Collection Layer:                                     │  │
 │ │       - Read GPS, accelerometer, gyroscope, speed sensor data    │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │   2. Violation Detection Layer:                                 │  │
 │ │       - Speeding detection                                      │  │
 │ │       - Reckless driving detection                              │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │   3. Data Logging Layer:                                        │  │
 │ │       - Log violations to SD card                               │  │
 │ │       - Trigger video recording (optional)                      │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │   4. Communication & User Interface Layer:                      │  │
 │ │       - Wi-Fi/Bluetooth data sync                               │  │
 │ │       - Smartphone app/web dashboard for data viewing            │  │
 │ │       - Real-time alerts (optional)                             │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 └────────────────────────────────────────────────────────────────────┘