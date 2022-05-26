from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN)

print('Hello!')

while True:
    v = button.value()
    led.value(not v)
    time.sleep(0.01)