from scapy.all import ICMP
from scapy.all import sr
from scapy.all import IP

def checkPing():
    src_ip = "192.168.1.10"
    dst_ip = "www.google.com"

    ip_layer = IP(src=src_ip,dst=dst_ip)

    print(ip_layer.show())

    


if __name__ == '__main__':
    checkPing()
