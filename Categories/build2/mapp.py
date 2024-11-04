import folium
from folium.plugins import HeatMap, MarkerCluster, TimestampedGeoJson
import pandas as pd
import random
import time

# Function to create the main map
def create_map():
    # Initialize map centered on a sample location
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=15, tiles="Stamen Terrain")
    
    # 1. Real-time GPS Tracking simulation
    def simulate_gps_tracking(map_obj, n_points=10):
        points = []
        lat, lon = 37.7749, -122.4194  # Starting point (San Francisco)
        
        # Simulate 10 GPS waypoints
        for i in range(n_points):
            lat += random.uniform(-0.001, 0.001)  # Simulate slight lat movement
            lon += random.uniform(-0.001, 0.001)  # Simulate slight lon movement
            points.append([lat, lon])
            folium.Marker(
                location=[lat, lon], 
                popup=f"Waypoint {i+1}",
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(map_obj)
            
            # Simulate real-time delay for dynamic update
            time.sleep(0.5)
        
        # Draw a line connecting the waypoints (trajectory)
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_obj)
        return points

    # 2. Field Boundary Overlay (GeoJSON)
    def add_field_boundary(map_obj):
        # Example GeoJSON for a simple rectangular field
        field_geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [[
                            [-122.414, 37.779], [-122.404, 37.779],
                            [-122.404, 37.769], [-122.414, 37.769],
                            [-122.414, 37.779]
                        ]]
                    },
                    "properties": {
                        "name": "Field 1"
                    }
                }
            ]
        }
        folium.GeoJson(field_geojson, name="Field Boundary").add_to(map_obj)

    # 3. Add a heatmap of tractor activity (waypoints)
    def add_heatmap(map_obj, points):
        HeatMap(points).add_to(map_obj)
    
    # 4. Add marker clustering for tractor activity points
    def add_marker_cluster(map_obj, points):
        marker_cluster = MarkerCluster().add_to(map_obj)
        for point in points:
            folium.Marker(point, popup="Activity Point").add_to(marker_cluster)
    
    # 5. Timestamped GeoJson for animated waypoints over time
    def add_timestamped_geojson(map_obj, points):
        features = [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [point[1], point[0]],
                },
                "properties": {
                    "time": f"2024-09-25T00:{i:02d}:00Z",
                    "popup": f"Waypoint {i+1}"
                }
            } for i, point in enumerate(points)
        ]
        timestamped_data = {
            "type": "FeatureCollection",
            "features": features
        }
        TimestampedGeoJson(timestamped_data, period="PT1M").add_to(map_obj)
    
    # Call the functions to add features to the map
    add_field_boundary(m)
    
    # Simulate real-time GPS tracking and get the waypoints
    gps_points = simulate_gps_tracking(m)
    
    # Add Heatmap and Marker Clustering based on GPS waypoints
    add_heatmap(m, gps_points)
    add_marker_cluster(m, gps_points)
    
    # Add animated waypoints over time
    add_timestamped_geojson(m, gps_points)
    
    # Save the final map as an HTML file
    m.save("tractor_map.html")
    print("Map has been created and saved as 'tractor_map.html'.")

# Create the interactive map
create_map()
