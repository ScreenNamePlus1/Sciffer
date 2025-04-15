from scapy.all import sniff, IP, TCP, UDP

target_port = 8022  # Replace with your port number
connected_ips = set()

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        if TCP in packet and (packet[TCP].sport == target_port or packet[TCP].dport == target_port):
            connected_ips.add(src_ip)
            connected_ips.add(dst_ip)
            print(f"TCP traffic on port {target_port} from/to: {src_ip} <-> {dst_ip}")
        elif UDP in packet and (packet[UDP].sport == target_port or packet[UDP].dport == target_port):
            connected_ips.add(src_ip)
            connected_ips.add(dst_ip)
            print(f"UDP traffic on port {target_port} from/to: {src_ip} <-> {dst_ip}")

sniff(filter=f"tcp port {target_port} or udp port {target_port}", prn=packet_callback, store=0)

print("\nIP addresses connected to port", target_port)
for ip in connected_ips:
    print(ip)
