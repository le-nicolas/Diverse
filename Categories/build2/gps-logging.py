import serial
import time

def log_gps():
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
    while True:
        line = ser.readline().decode('ascii', errors='replace')
        if line.startswith('$GPGGA'):
            gps_data = line.split(',')
            latitude = gps_data[2]
            longitude = gps_data[4]
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            time.sleep(1)
