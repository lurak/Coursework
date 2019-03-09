import folium


def get_map(places, path, location):

    m = folium.Map(
        location=location,
        zoom_start=12,
        tiles='Stamen Terrain'
    )
    for place in places:
        folium.Marker(
            location=list(map(int, list(place.coordinates))),
            popup=place.name,
            icon=folium.Icon(icon='cloud')
        ).add_to(m)
    m.save(path)