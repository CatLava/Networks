# python nslookup to add into shodan code
import socket
import re
import geol

web =  input("enter url :")
ips = socket.getaddrinfo(web, 80)
iplst = []
iplst2 = []
lst = []
master = []
for i in ips:
    iplst.append(i)
    for j in iplst:
        j = str(j)
        if not j.startswith('(<AddressFamily.AF_INET:'): continue
        iplst2.append(j)
for items in iplst2:
    m = items.split()
    lst.append(m)
    for i in lst:
        k = i[5][2:-2]
        master.append(k)
master = set(master)
print('Found IPs:', master)
def lst():
    return master
for i in master:
    kk = geol.loc(i)
    print(kk)
