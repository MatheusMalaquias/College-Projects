#Wind Chill (°F) = 35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16
import math

def wind_chill_calculate (temperature, speed):
    wind_chill_fahrenheit =  35.74 + 0.6215 * temperature - 35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16
    return wind_chill_fahrenheit

def convert_celsius (celsius):
    fahrenheit =  (celsius * 9/5) + 32
    return fahrenheit

temperature_user = float(input ("What is the temperature? "))
format_temperature = input("Fahrenheit or Celsius (F/C)? ")

if format_temperature.upper() == 'F':
    for wind_speed in range (5,61,5):
        wind_chill = wind_chill_calculate (temperature_user, wind_speed)
        print (f"At temperature {temperature_user}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}°F")

elif format_temperature.upper() == 'C':
    fahrenheit_temperature = convert_celsius (temperature_user)
    for wind_speed in range (5,61,5):
        wind_chill = wind_chill_calculate (fahrenheit_temperature, wind_speed)
        print (f"At temperature {fahrenheit_temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}°F ")