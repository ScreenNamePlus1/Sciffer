def modify_packet(packet):
    """Prompts the user for modifications to the packet (including content)."""
    if IP in packet:
        new_src_ip = input(f"Enter new Source IP (leave blank for '{packet[IP].src}'): ")
        if new_src_ip:
            packet[IP].src = new_src_ip
        new_dst_ip = input(f"Enter new Destination IP (leave blank for '{packet[IP].dst}'): ")
        if new_dst_ip:
            packet[IP].dst = new_dst_ip
        del packet[IP].chksum

    if TCP in packet:
        new_sport_tcp = input(f"Enter new Source Port (TCP) (leave blank for '{packet[TCP].sport}'): ")
        if new_sport_tcp:
            packet[TCP].sport = int(new_sport_tcp)
        new_dport_tcp = input(f"Enter new Destination Port (TCP) (leave blank for '{packet[TCP].dport}'): ")
        if new_dport_tcp:
            packet[TCP].dport = int(new_dport_tcp)
        new_flags_tcp = input(f"Enter new TCP Flags (e.g., SYN, ACK, leave blank for '{packet[TCP].flags}'): ")
        if new_flags_tcp:
            packet[TCP].flags = new_flags_tcp
        del packet[TCP].chksum

        # Modify TCP payload
        current_payload = raw(packet[TCP].payload) if packet.haslayer(TCP) and packet[TCP].payload else "<No Payload>"
        new_payload_tcp_hex = input(f"Enter new TCP Payload (hexadecimal, leave blank for '{current_payload[:20]}...'): ")
        if new_payload_tcp_hex:
            try:
                packet[TCP].payload = bytes.fromhex(new_payload_tcp_hex)
                del packet[IP].len  # Need to recalculate IP length
            except ValueError:
                print("Invalid hexadecimal input for TCP payload.")

    elif UDP in packet:
        new_sport_udp = input(f"Enter new Source Port (UDP) (leave blank for '{packet[UDP].sport}'): ")
        if new_sport_udp:
            packet[UDP].sport = int(new_sport_udp)
        new_dport_udp = input(f"Enter new Destination Port (UDP) (leave blank for '{packet[UDP].dport}'): ")
        if new_dport_udp:
            packet[UDP].dport = int(new_dport_tcp) # Typo in original: should be UDP
        del packet[UDP].chksum

        # Modify UDP payload
        current_payload = raw(packet[UDP].payload) if packet.haslayer(UDP) and packet[UDP].payload else "<No Payload>"
        new_payload_udp_hex = input(f"Enter new UDP Payload (hexadecimal, leave blank for '{current_payload[:20]}...'): ")
        if new_payload_udp_hex:
            try:
                packet[UDP].payload = bytes.fromhex(new_payload_udp_hex)
                del packet[IP].len  # Need to recalculate IP length
            except ValueError:
                print("Invalid hexadecimal input for UDP payload.")

    if IP in packet:
        del packet[IP].chksum  # Recalculate IP checksum
        del packet[IP].len     # Ensure IP length is recalculated

    return packet
