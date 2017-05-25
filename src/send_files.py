from socket import *
import os
import pexpect
passwd = 'uiuc105'

fp = open("config.txt","r")
for item in fp.readlines():	
    ssh_notice = 'Are you sure you want to continue connecting'
    p=pexpect.spawn('ssh ' + item.strip() + ' ls')
    i=p.expect([ssh_notice,'password:',pexpect.EOF])
    if i==0:
        p.sendline('yes')
        i=p.expect([ssh_notice,'password:',pexpect.EOF], timeout = 2)
fp.close()

fp = open("config.txt","r")
for item in fp.readlines():	
    cmd = "sshpass -p %s scp new_connect.py pi@%s:~/Desktop/research/tmp" % (passwd, item.strip())    
    os.system(cmd)
    cmd = "sshpass -p %s scp broadcast.py pi@%s:~/Desktop/research/tmp" % (passwd, item.strip())    
    os.system(cmd)
    print "here!"
fp.close()
