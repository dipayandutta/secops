from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr 

def checkPing(source, destination):
    source_address = source
    destination_address = destination

    ip_layer=IP(src=source_address,dst=destination_address)
    print(ip_layer.show())

    # send ICMP packets
    icmp_req = ICMP(id=100)
    print("====ICMP Request Send=====")
    print(icmp_req.show()) # packet type is echo request

    packet = ip_layer/icmp_req
    print("====Packet====")
    print(packet.show())

if __name__ == '__main__':
    checkPing("192.168.100.2","kolkatapolice.gov.in")
