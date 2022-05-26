import machine, neopixel
from machine import Timer

np = neopixel.NeoPixel(machine.Pin(14), 180)
tim1 = Timer(1)

counter = 0
COLOR  = (10, 10, 255)

def tick(t):
    global counter
    np.fill((0, 0, 0))
    
    for i in range(15):
        r = int(COLOR[0] * (i / 15.0))
        g = int(COLOR[1] * (i / 15.0))
        b = int(COLOR[2] * (i / 15.0))
        np[counter + i] = (r, g, b)
    
    np.write()
    counter += 1
    if counter == 160:
        counter = 0

tim1.init(period=10, mode=Timer.PERIODIC, callback=tick)