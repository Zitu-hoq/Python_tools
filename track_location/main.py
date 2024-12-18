import os
import phonenumbers
import opencage
import folium


from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv, dotenv_values


load_dotenv()
key = os.getenv("api_key")      # replace with your opencage api key
phoneNumber = input("[+]Enter Target phone number with country code:\t")


tPhoneNumber = phonenumbers.parse(phoneNumber)
countryName = geocoder.description_for_number(tPhoneNumber, "en")
network_provider = carrier.name_for_number(tPhoneNumber, "en")
timeZone = timezone.time_zones_for_number(tPhoneNumber)


geocoder = OpenCageGeocode(key)
locationObj = geocoder.geocode(countryName)
lat = locationObj[0]['geometry']['lat']
lng = locationObj[0]['geometry']['lng']

locationDetails = geocoder.reverse_geocode(lat, lng)
location = locationDetails[0]['formatted']

print(f"SIM Card Provider:\t{network_provider}\nTime Zone:\t{timeZone}\nLocation:\t{location}\n")

isPrint = int(input("[+]Enter 1 to see in Map\t"))
if(isPrint==1):
    targetMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(targetMap)
    targetMap.save("location.html")
    print("[+] Map saved in location.html")