import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(14), 8)

np[0] = (128, 0, 0)
np[1] = (0, 128, 0)
np[2] = (0, 0, 128)

np.write()