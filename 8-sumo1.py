from sumolib import *
import time

print("Hello sumo!")

start = Start1()
ledRgb = LedRgb1()
grd1, grd2, grd3, grd4 = grds_init()
dist1, dist2, dist3, dist4 = dists_init()

ledRgb.value = Color.BLUE

while True:
    print('GRD1:', grd1, 'GRD2:', grd2, 'GRD3:', grd3, 'GRD4:', grd4)
    values = (dist1.value, dist2.value, dist3.value)
    print('DIST1: %0.2f, DIST2: %0.2f, DIST3: %0.2f' % values)
    time.sleep(0.5)
