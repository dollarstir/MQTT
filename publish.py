import paho.mqtt.publish as publish

publish.single("UCC/Dollartir", "boo!", hostname="localhost", port=4000)