from machine import Pin, ADC
import time

adc = ADC(Pin(34))

while True:
    print(adc.read(), adc.read_uv())
    time.sleep(0.5)