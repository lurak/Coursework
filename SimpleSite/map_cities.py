import folium


def get_map(place, path):

    m = folium.Map(
        location=(place.latitude, place.longitude),
        zoom_start=12,

    )

    folium.Marker(
        location=(place.latitude, place.longitude),
        popup=place.name,
        icon=folium.Icon(icon='cloud')
    ).add_to(m)
    m.save(path)
