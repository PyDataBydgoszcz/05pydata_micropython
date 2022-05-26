import network
import http_client

st = network.WLAN(network.STA_IF)
st.active(True)

st.connect('MicroPython', '123456789')
while not st.isconnected():
    pass

print('Connected', st.ifconfig())

url = 'http://192.168.8.100:8080/person'

r = http_client.get(url, timeout=5)
print(r.status_code)
print(r.text)
print(r.json())
