# just a script for starting processes on other machines
from socket import *
'''
import os 

passwd = 'uiuc105'

fp = open("config.txt","r")
for item in fp.readlines():
    #print item.strip()
    cmd = "sshpass -p %s ssh pi@%s 'pushd ~/Desktop/research; python new_connect.py'" % (passwd, item.strip())    
    os.system(cmd)    
fp.close()
'''
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
data = ''
s.sendto(data, ('192.168.12.255', 8888))
s.sendto(data, ('192.168.12.255', 8888))
s.sendto(data, ('192.168.12.255', 8888))
s.close()
