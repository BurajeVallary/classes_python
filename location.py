
import phonenumbers
from phonenumbers import geocoder

phone_number1 =phonenumbers.parse("+254758797430")
phone_number2 =phonenumbers.parse("+16673836619")
phone_number3 =phonenumbers.parse("+18453701206")
phone_number4 =phonenumbers.parse("+254713171363")
phone_number5 =phonenumbers.parse("+254713724350")

print ("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
print(geocoder.description_for_number(phone_number5,"en"))

