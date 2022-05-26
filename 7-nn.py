from ulab import numpy as np
import time

import machine
machine.freq(240000000)

w1 = np.load('w1.npy')
b1 = np.load('b1.npy')
w2 = np.load('w2.npy')
b2 = np.load('b2.npy')
x = np.load('x.npy')


start = time.ticks_us() 

y = np.dot(w1,x) + b1
np.maximum(y,np.zeros(len(y)))
y = np.dot(w2,y) + b2

end = time.ticks_us()

print(y)
print(time.ticks_diff(end, start))

