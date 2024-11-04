from folium.plugins import TimestampedGeoJson

data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-122.4194, 37.7749],
            },
            "properties": {
                "time": "2024-09-25T00:00:00Z",
                "popup": "Start point",
            },
        },
        # Add more features with timestamps
    ],
}
TimestampedGeoJson(data).add_to(m)
