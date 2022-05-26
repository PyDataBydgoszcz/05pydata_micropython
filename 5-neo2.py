import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(14), 180)

while True:

    for i in range(128):
        np.fill((i, 128-i, 0))
        np.write()
        time.sleep(0.02)
        
    for i in range(128):
        np.fill((128-i, 0, i))
        np.write()
        time.sleep(0.02)
        
    for i in range(128):
        np.fill((0, i, 128-i))
        np.write()
        time.sleep(0.02)