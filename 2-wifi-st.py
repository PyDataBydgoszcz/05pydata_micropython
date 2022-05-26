import network

ssid = 'MicroPython'
password = '123456789'

st = network.WLAN(network.STA_IF)
st.active(True)

print(st.scan())

#st.connect(ssid, password)
st.connect('MicroPython', '123456789')

while not st.isconnected():
    pass

print('Connected')
print(st.ifconfig())
