from pydoc import cli
from tabnanny import verbose
import scapy.all as scapy
import bottele



    
target_ip = '192.168.1.1/24'

arp = scapy.ARP(pdst = target_ip)

ether = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff" )

paquete = ether/arp

respuesta = scapy.srp(paquete, timeout = 2, verbose=0) [0]

clients= []

for enviado,recivido in respuesta:
    clients+= [[recivido.psrc,recivido.hwsrc]]

totalIp=len(clients)
b=0

for i in range (totalIp):
    if clients[i][1] == 'd0:67:e5:e7:1b:8d':
        b=1
    print("IP: {} MAC: {}". format(clients[i][0], clients[i][1]))

if b==1:
    bottele.telegram_bot_sendtext("tamy conectada")
else:
    bottele.telegram_bot_sendtext("tamy no conectada")
    


