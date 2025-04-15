# Scapy Port Sniffer (sciffer.py)

This Python script uses the `scapy` library to capture network packets and identify the IP addresses communicating on a specified port.

## What this script does:

* **Captures network traffic:** It listens to all network interfaces for incoming and outgoing packets.
* **Filters by port:** It specifically looks for TCP and UDP packets where either the source or destination port matches the `target_port` defined in the script.
* **Extracts IP addresses:** For the packets matching the port filter, it extracts the source and destination IP addresses.
* **Prints connected IPs:** It displays the IP addresses that have been seen communicating on the specified port.

## How to use:

1.  **Save the code:** Save the Python code provided earlier as `scapy_sniffer.py`.

2.  **Install `scapy` (if you haven't already):**
    ```bash
    pip install scapy
    ```
    You might have already done this based on our previous conversation.

3.  **Run the script with root privileges:** Capturing raw network packets requires elevated permissions. In most Linux-like environments (including Termux), you'll need to run the script as the root user.

    * **In Termux:**
        ```bash
        su
        python sciffer.py
        ```
        You might be prompted for a root password.

    * **On other Linux systems:** You might need to use `sudo`:
        ```bash
        sudo python sciffer.py
        ```
        You'll likely be asked for your user password.

4.  **Observe the output:** The script will start listening for traffic on the specified `target_port`. As packets matching the filter are captured, it will print the source and destination IP addresses involved in that communication. After you stop the script (usually by pressing `Ctrl+C`), it will print a summary of the unique IP addresses that were seen communicating on that port.

## Code Explanation:

```python
from scapy.all import sniff, IP, TCP, UDP

target_port = 8022  # Replace with the port number you want to monitor
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

 * from scapy.all import sniff, IP, TCP, UDP: Imports necessary functions and classes from the scapy library.
   * sniff: The function used to capture network packets.
   * IP: Represents the IP layer of a network packet, containing source and destination IP addresses.
   * TCP: Represents the TCP layer, containing source and destination ports.
   * UDP: Represents the UDP layer, also containing source and destination ports.
 * target_port = 8022: Defines the port number you want to monitor. Remember to change this to the port you are interested in.
 * connected_ips = set(): Initializes an empty set to store the unique IP addresses that communicate on the target port. Using a set automatically handles duplicates.
 * packet_callback(packet): This function is called for each captured packet.
   * It checks if the packet has an IP layer (if IP in packet).
   * It extracts the source (src_ip) and destination (dst_ip) IP addresses.
   * It then checks if the packet is TCP or UDP and if either the source port (packet[TCP].sport or packet[UDP].sport) or the destination port (packet[TCP].dport or packet[UDP].dport) matches the target_port.
   * If the port matches, the source and destination IP addresses are added to the connected_ips set, and a message indicating the traffic is printed.
 * sniff(...): This is the core function for capturing packets.
   * filter=f"tcp port {target_port} or udp port {target_port}": This is a Berkeley Packet Filter (BPF) string that tells scapy to only capture TCP or UDP packets involving the target_port. This filtering happens at a low level, making the capture more efficient.
   * prn=packet_callback: This specifies the packet_callback function to be executed for each captured packet.
   * store=0: This tells scapy not to store all captured packets in memory, which is more efficient for continuous monitoring.
 * print("\nIP addresses connected to port", target_port) and the following loop: After the sniffing is stopped, this part iterates through the connected_ips set and prints each unique IP address that was involved in communication on the target_port.
Important Notes:
 * Permissions: Running this script requires root or administrator privileges because it needs direct access to the network interface.
 * Termux: In Termux, you'll likely need to use the su command to gain root access before running the script.
 * Dependencies: Make sure you have the scapy library installed (pip install scapy).
 * Network Activity: You will only see IP addresses that are actively communicating on the specified port while the script is running.
 * Stopping the script: To stop the script, press Ctrl+C in your terminal.
This readme should provide you with a good understanding of the script and how to run it. Let me know if you have any other questions!
