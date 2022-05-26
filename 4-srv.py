import network
from microWebSrv import MicroWebSrv
from machine import Pin
import esp32

st = network.WLAN(network.STA_IF)
st.active(True)

st.connect('MicroPython', '123456789')
while not st.isconnected():
    pass

print('Connected', st.ifconfig())

led = Pin(2, Pin.OUT)

@MicroWebSrv.route('/ping')
def handlerPing(httpClient, httpResponse, args=None):
    print('/ping', args)
    httpResponse.WriteResponseJSONOk('pong')

@MicroWebSrv.route('/led/<state>')
def handlerPing(httpClient, httpResponse, args=None):
    print('/led', args)
    state = args['state']
    led.value(state)
    httpResponse.WriteResponseJSONOk('Ok')
    
@MicroWebSrv.route('/sensors')
def handlerPing(httpClient, httpResponse, args=None):
    print('/sensors', args)
    hall = esp32.hall_sensor()
    fahrenheit = esp32.raw_temperature()
    celsius = (fahrenheit - 32) * 5/9
    httpResponse.WriteResponseJSONOk([hall, celsius])

mws = MicroWebSrv()
mws.Start(threaded=True)


    
    
