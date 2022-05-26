import esp32

hall = esp32.hall_sensor()
fahrenheit = esp32.raw_temperature()
celsius = (fahrenheit - 32) * 5/9

print(hall, celsius)