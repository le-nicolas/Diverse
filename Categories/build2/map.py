import folium

# Function to create a map and add GPS waypoints
def create_map(waypoints):
    # Initialize the map at the starting point (first waypoint)
    map_center = waypoints[0]  # Center the map on the first point
    m = folium.Map(location=map_center, zoom_start=15)
    
    # Plot each waypoint on the map
    for i, point in enumerate(waypoints):
        folium.Marker(
            location=point,
            popup=f"Waypoint {i+1}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
    
    # Optionally, connect the waypoints with lines (polylines)
    folium.PolyLine(waypoints, color="red", weight=2.5, opacity=1).add_to(m)
    
    # Save map to an HTML file
    m.save("virtual_map.html")
    print("Map has been created and saved as 'virtual_map.html'.")

# Example list of waypoints (latitude, longitude)
waypoints = [
    (37.7749, -122.4194),  # San Francisco
    (37.7849, -122.4094),  # Another point in SF
    (37.7949, -122.3994),  # Another point in SF
    (37.8049, -122.3894)   # Another point in SF
]

# Create the map with waypoints
create_map(waypoints)
