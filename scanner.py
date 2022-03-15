from pydoc import cli
from tabnanny import verbose
import scapy.all as scapy


target_ip = '192.168.1.1/24'

arp = scapy.ARP(pdst = target_ip)

ether = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff" )

paquete = ether/arp

respuesta = scapy.srp(paquete, timeout = 2, verbose=0) [0]

clients= []

for enviado,recivido in respuesta:
    clients+= [[recivido.psrc,recivido.hwsrc]]

totalIp=len(clients)

for i in range (totalIp):
    print("IP: {} MAC: {}". format(clients[i][0], clients[i][1]))
