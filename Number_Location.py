import phonenumbers

import folium

from my_Numbers import number

from phonenumbers import geocoder

Key = '455998a70d794a19b412f988e1357366'

someNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(someNumber, "en")
print(yourLocation)

# Get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)

folium.Marker([lat, lng], popup= yourLocation).add_to((myMap))

# asve map in html file

myMap.save("myLocation.html")
