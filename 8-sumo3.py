from sumolib import *
import time

print("Hello sumo!")

TRESHOLD = 0.5

start = Start1()
ledRgb = LedRgb1()
grd1, grd2, grd3, grd4 = grds_init()
dist1, dist2, dist3, dist4 = dists_init()

motor1, motor2 = motors_init()
motor1.power = 0.7
motor2.power = 0.7

ledRgb.value = Color.RED

start.waitFor()

ledRgb.value = Color.GREEN

while True:
    if dist1.value > TRESHOLD and dist2.value > TRESHOLD:
        motor1.forward()
        motor2.forward()
        ledRgb.value = Color.WHITE
    elif dist1.value > TRESHOLD:
        motor1.backward()
        motor2.forward()
        ledRgb.value = Color.CYAN
    elif dist2.value > TRESHOLD:
        motor1.forward()
        motor2.backward()
        ledRgb.value = Color.PURPLE
    else:
        motor1.stop()
        motor2.stop()
        ledRgb.value = Color.GREEN
    time.sleep(0.03)
        
        
        