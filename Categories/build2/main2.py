#GPIO
import RPi.GPIO as GPIO
import time

# Setup GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
motor_pin = 17
GPIO.setup(motor_pin, GPIO.OUT)
pwm = GPIO.PWM(motor_pin, 100)
pwm.start(0)

# Motor control function
def set_motor_speed(speed):
    pwm.ChangeDutyCycle(speed)

# Example usage
set_motor_speed(50)  # Set motor speed to 50% power
time.sleep(5)
pwm.stop()
GPIO.cleanup()

#PID
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, setpoint, actual):
        error = setpoint - actual
        self.integral += error
        derivative = error - self.previous_error
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        self.previous_error = error
        return output


#GPS logging
import serial
import csv
import time

# Open serial port for GPS
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Open CSV file to log data
with open('trajectory.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Latitude', 'Longitude'])  # Headers
    
    while True:
        line = ser.readline().decode('ascii', errors='replace')
        if line.startswith('$GPGGA'):
            gps_data = line.split(',')
            latitude = gps_data[2]
            longitude = gps_data[4]
            timestamp = time.time()
            writer.writerow([timestamp, latitude, longitude])  # Log data
            print(f"Logged: {latitude}, {longitude}")
        time.sleep(1)


#waypoint navigation
import math

def compute_distance(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points
    R = 6371000  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

# Check if the tractor is within a tolerance distance of the next waypoint
def navigate_to_waypoint(current_lat, current_lon, waypoint_lat, waypoint_lon):
    tolerance = 2.0  # meters
    distance_to_waypoint = compute_distance(current_lat, current_lon, waypoint_lat, waypoint_lon)
    
    if distance_to_waypoint > tolerance:
        # Implement control logic to move towards the waypoint
        adjust_heading()  # PID adjustment to steer the tractor
        adjust_speed()    # Adjust speed to match the distance to the waypoint

