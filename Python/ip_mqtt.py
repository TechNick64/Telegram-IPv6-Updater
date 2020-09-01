import netifaces as ni #pip3 install netifaces
import paho.mqtt.client as paho #pip3 install paho-mqtt

broker="IP"
port=1883

ni.ifaddresses('ens18') #Adapter
ipv6 = ni.ifaddresses('ens18')[ni.AF_INET6][1]['addr']
print(ipv6)

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client= paho.Client("Client_Name")
client.on_publish = on_publish
client.connect(broker,port)
ret= client.publish("Dir/ipv6",ipv6)
