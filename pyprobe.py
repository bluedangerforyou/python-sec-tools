from scapy.all import *
interface = 'mon0'
probeReqs = []
def probesniff(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netName not in probeReqs:
            probeReq.append(netName)
            print '[+] We detected a new probe request: ' + netName
sniff(iface=interface, prn=probsniff)
    
