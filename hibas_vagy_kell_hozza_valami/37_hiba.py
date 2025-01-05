from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

place = input("Enter the Place Name: ")
location = geolocator.geocode(place)

data = location.raw
loc_data = data['display_name'].split()
print("Full Location")
print(loc_data)
print("Zip code:", loc_data[-2])