import paho.mqtt.client as mqtt
import time
import pyowm

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
        


    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection
client = mqtt.Client()
client.on_connect = on_connect
client.connect("104.248.163.70", 1883, 60)
client.loop_start()  # start the loop





api_key = "74c8a5ed2adad61f64819dfed080f662"
owm = pyowm.OWM(api_key)

observation = owm.weather_at_place("Accra,Ghana")
w = observation.get_weather()
h=w.get_temperature()
print(h["temp"])
while Connected != True:  # Wait for connection
    time.sleep(0.1)
try:
    while True:
        
        message1 = str(input("Message:"))
        message= message1 + str(w)
        client.publish("UCC/Dollarstir", message)
            

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()