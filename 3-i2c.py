from machine import Pin, SoftI2C
import time

i2c = SoftI2C(scl=Pin(12), sda=Pin(13), freq=100000)

print(i2c.scan())

i2c.writeto(93, bytearray([0x20, 0x90]))

time.sleep(0.1)

data = i2c.readfrom_mem(93, 0x28 | 0x80, 3)

pressure = (data[2] * 65536 + data[1] * 256 + data[0]) / 4096.0

print(pressure)