import folium
from geopy.geocoders import Nominatim
import requests

def get_coordinate(city):
    locator = Nominatim(user_agent="agent")
    location = locator.geocode(city)
    return (location.latitude, location.longitude)

def get_polygon(city):
    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={city}&format=json&polygon=1&limit=1&polygon_geojson=1")
    json = response.json()
    polygon = json[0]["geojson"]["coordinates"][0]
    new_polygon = []
    for item in polygon:
        new_polygon.append((item[1], item[0]))

    return new_polygon

def display_map(city):
    coordinate = get_coordinate(city)
    m = folium.Map(location=coordinate)
    return m


if __name__ == "__main__":
    print(get_coordinate("Annecy"))
    print(get_polygon("Annecy"))
    display_map("Annecy").render()
