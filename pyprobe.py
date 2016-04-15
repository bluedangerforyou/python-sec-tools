from scapy.all import *

interface = raw_input("Enter your monitor mode interface- i.e wlan0mon: ")
probeReq = []
def probsniff(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netName not in probeReq:
            probeReq.append(netName)
            print '[+] We detected a new probe request: ' + netName
sniff(iface=interface, prn=probsniff)
