import machine, neopixel
from machine import Timer

np = neopixel.NeoPixel(machine.Pin(14), 180)
tim1 = Timer(1)

counter = 0

def tick(t):
    global counter
    if counter % 3 == 0:
        np.fill((128, 0, 0))
    elif counter % 3 == 1:
        np.fill((0, 128, 0))
    else:
        np.fill((0, 0, 128))
    np.write()
    counter += 1
    print(counter)

tim1.init(period=2000, mode=Timer.PERIODIC, callback=tick)