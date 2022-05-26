import machine, neopixel
from machine import Timer

np = neopixel.NeoPixel(machine.Pin(14), 180)
tim1 = Timer(1)

counter = 0

def getColor(i):
    a = i%128
    b = int(i/128)
    
    if b % 3 == 0:
        return (a, 128-a, 0)
    elif b % 3 == 1:
        return (128-a, 0, a)
    else:
        return (0, a, 128-a)

def tick(t):
    global counter
    color = getColor(counter)
    
    for i in range(180):
        color = getColor(counter+i*5)
        np[i] = color 
    
    np.write()
    counter += 1


tim1.init(period=30, mode=Timer.PERIODIC, callback=tick)