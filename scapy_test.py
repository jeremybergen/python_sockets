from scapy.all import *

# packet = Ether()/IP(dst='8.8.8.8')
# print(f"{packet.summary()}")
payload = "Hello"
packet = IP(dst='8.8.8.8')/ICMP()/payload
response = sr1(packet)

hexdump(response)