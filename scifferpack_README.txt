# Scifferpack.py - Interactive Packet Capture and Modification Tool

## Overview

`scifferpack.py` is a Python script that utilizes the `scapy` library to provide an interactive way to capture, inspect, modify, and send network packets. It allows you to:

1.  **Capture Packets:** Sniff a specified number of network packets.
2.  **Inspect Packets:** View a summary and detailed information of the captured packets.
3.  **Modify Packets:** Interactively change various fields in the captured packets, including source and destination IP addresses, source and destination ports (TCP/UDP), TCP flags, and the raw payload (in hexadecimal format).
4.  **Send Packets:** Choose to send the modified packet using either `scapy.send()` (layer 3) or `scapy.sendp()` (layer 2).

**Warning:** This tool can be powerful and should be used responsibly and ethically. Sending modified network traffic on networks you do not own or have permission to test on can have unintended and potentially harmful consequences.

## Prerequisites

* **Python 3:** Ensure you have Python 3 installed on your system.
* **Scapy:** The `scapy` library is required. You can install it using pip:
    ```bash
    pip install scapy
    ```
    **Note:** Capturing and sending raw network packets often requires root or administrator privileges.

## Usage

1.  **Save the script:** Save the Python code as `scifferpack.py`.

2.  **Run the script with appropriate privileges:**
    * **Linux/macOS:** Open your terminal and run with `sudo`:
        ```bash
        sudo python scifferpack.py
        ```
    * **Termux:** Open Termux and gain root access (if possible) before running:
        ```bash
        su
        python scifferpack.py
        ```
    * **Windows:** Open Command Prompt as an administrator and run:
        ```bash
        python scifferpack.py
        ```

3.  **Follow the prompts:**
    * The script will first ask you how many packets you want to capture. Enter a number (e.g., `1` to modify the first captured packet).
    * It will then display a summary of the captured packet(s).
    * You will be prompted to enter the number of the packet you wish to modify.
    * The script will show the details of the selected packet and then ask you to enter new values for various header fields (IP addresses, ports, TCP flags) and the payload (in hexadecimal). Leave a field blank to keep its original value.
    * Finally, you will be asked if you want to send the modified packet and to choose a sending method (`send()` for layer 3 or `sendp()` for layer 2).

## Script Description

The `scifferpack.py` script contains the following functions:

* **`display_packet(packet)`:** Displays a user-friendly summary of a given `scapy` packet.
* **`modify_packet(packet)`:** Takes a `scapy` packet, prompts the user for modifications to various header fields (IP, TCP, UDP) and the payload (in hexadecimal), and returns the modified packet.
* **`send_packet_prompt(packet)`:** Asks the user if they want to send the provided packet and, if so, prompts for the sending method (`send()` or `sendp()`) before sending it.
* **`capture_and_modify()`:** This is the main function that orchestrates the packet capture, selection, modification, and sending processes. It prompts the user for the number of packets to capture, displays them, asks which one to modify, calls `modify_packet()` for user input, and then calls `send_packet_prompt()` to handle sending.

## Important Notes

* **Root/Administrator Privileges:** Capturing and sending raw network packets typically requires elevated privileges. If you encounter permission errors, ensure you are running the script with the necessary rights.
* **Payload Modification:** The script allows modification of the TCP and UDP payload by entering hexadecimal values. Ensure you understand the format and the implications of altering the payload for the specific network protocol you are working with.
* **Sending Methods:**
    * `send(packet)`: Sends packets at layer 3 (IP layer). It relies on the operating system's networking stack to handle lower-level details like Ethernet headers.
    * `sendp(packet)`: Sends packets at layer 2 (Ethernet layer). This gives you more control over the entire packet structure, including the MAC addresses. It requires the packet to have an Ethernet layer.
* **Error Handling:** The script includes basic error handling for invalid input (e.g., non-numeric input where expected, invalid hexadecimal payload).
* **Ethical Use:** Use this tool responsibly and only on networks and systems you have explicit permission to test. Unauthorized use can have serious consequences.

This readme provides a comprehensive overview of the `scifferpack.py` script and instructions on how to use it. Remember to exercise caution and ethical considerations when working with network packets.
