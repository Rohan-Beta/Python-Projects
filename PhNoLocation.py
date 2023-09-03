# phone number location

import phonenumbers
from phonenumbers import geocoder

ph1 = phonenumbers.parse("+918017") // put the number

print("Phone Number Location:")
print(geocoder.description_for_number(ph1 , "en")) // print the phone number location
