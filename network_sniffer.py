from scapy.all import sniff
from scapy.layers.inet import IP

packet_count = 0

def packet_callback(packet):
    global packet_count

    if packet.haslayer(IP):
        packet_count += 1

        print("\n" + "=" * 50)
        print(f"Packet Number : {packet_count}")
        print(f"Source IP     : {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol      : {packet[IP].proto}")
        print(f"Packet Length : {len(packet)} bytes")
        print("=" * 50)

print("Network Sniffer Started...")
print("Press CTRL+C to stop.")

sniff(prn=packet_callback, store=False)