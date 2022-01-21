from pydoc import cli
from tabnanny import verbose
from scapy.all import *
target_ip = '192.168.1.1/24'

arp =ARP(pdst = target_ip)

ether =Ether(dst = "ff:ff:ff:ff:ff:ff" )

paquete = ether/arp

respuesta = srp(paquete, timeout = 2, verbose=0) [0]

clients= []

for enviado,recivido in respuesta:
    clients+= [[recivido.psrc,recivido.hwsrc]]

totalIp=len(clients)

for i in range (totalIp):
    print("IP: {} MAC: {}". format(clients[i][0], clients[i][1]))
