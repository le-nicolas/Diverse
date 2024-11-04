# Define geofence boundary (latitude and longitude)
GEOFENCE_BOUNDARY = {
    "min_lat": 37.7749,  # Example values
    "max_lat": 37.7849,
    "min_lon": -122.4194,
    "max_lon": -122.4094
}

def check_geofence():
    current_location = vehicle.location.global_frame

    # Check if the drone is out of bounds
    if not (GEOFENCE_BOUNDARY["min_lat"] <= current_location.lat <= GEOFENCE_BOUNDARY["max_lat"] and
            GEOFENCE_BOUNDARY["min_lon"] <= current_location.lon <= GEOFENCE_BOUNDARY["max_lon"]):
        print("Drone is out of geofence boundary! Returning to home...")
        return_to_home()

# Adding geofencing to the main loop
while True:
    check_failsafe_conditions()
    check_geofence()  # Check geofence
    time.sleep(1)
