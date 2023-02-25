import phonenumbers
import opencage
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import timezone,carrier,geocoder,geodata,length_of_geographical_area_code,connects_to_emergency_number
number=input("enter your number")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
location=geocoder.description_for_number(phone,"en")
import opencage
key="key here"
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(results)
print(phone)
print(time)
print(carr)
print(reg)
print(location)
print(lat,lng)
mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("mylocation.html")

