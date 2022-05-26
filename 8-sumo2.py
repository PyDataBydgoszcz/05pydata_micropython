from sumolib import *
import time

print("Hello sumo!")

start = Start1()
ledRgb = LedRgb1()
grd1, grd2, grd3, grd4 = grds_init()
dist1, dist2, dist3, dist4 = dists_init()

motor1, motor2 = motors_init()
motor1.power = 0.7
motor2.power = 0.7

ledRgb.value = Color.RED

while True:
    if start.value:
        motor1.forward()
        motor2.forward()
        #motor1.backward()
        #motor2.backward()
        ledRgb.value = Color.GREEN
    else:
        motor1.stop()
        motor2.stop()
        ledRgb.value = Color.RED
    time.sleep(0.1)

