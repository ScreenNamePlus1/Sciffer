# <img src="path/to/your/project-logo.png" alt="Sciffer Project Logo" width="150"> Sciffer - Interactive Network Packet Toolkit

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Scapy](https://img.shields.io/badge/Scapy-2.6+-brightgreen.svg)](https://scapy.net/)
[![GitHub Stars](https://img.shields.io/github/stars/YourUsername/Sciffer.svg?style=social&label=Stars)](https://github.com/YourUsername/Sciffer)
[![GitHub Forks](https://img.shields.io/github/forks/YourUsername/Sciffer.svg?style=social&label=Fork)](https://github.com/YourUsername/Sciffer)

> An interactive command-line tool leveraging the power of Scapy for capturing, inspecting, modifying, and sending network packets. Dive deep into network traffic and experiment with packet manipulation in a user-friendly way.

---

## 🛠️ Features

* **Interactive Packet Capture:** Sniff a specified number of network packets directly from your terminal.
* **Detailed Packet Inspection:** View summaries and detailed layer-by-layer information of captured packets.
* **On-the-Fly Packet Modification:** Interactively edit various packet headers (IP addresses, TCP/UDP ports, TCP flags) and the raw payload (in hexadecimal format).
* **Flexible Sending Options:** Choose to transmit modified packets at Layer 3 (IP) using `send()` or Layer 2 (Ethernet) using `sendp()`.
* **Clear User Interface:** Simple and intuitive command-line prompts guide you through the packet manipulation process.
* **Educational and Experimental:** Ideal for learning about network protocols, debugging network issues, and experimenting with packet crafting.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.6+**
* **Scapy (version 2.6 or higher)**

### Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [https://github.com/YourUsername/Sciffer.git](https://github.com/YourUsername/Sciffer.git)
    cd Sciffer
    ```

2.  **Install Scapy:**
    ```bash
    pip install scapy
    ```

### Running the Tool

Navigate to the project directory in your terminal and run the script with appropriate privileges (root or administrator are often required for raw socket operations):

```bash
sudo python scifferpack.py  # Linux/macOS
python scifferpack.py       # Windows (run as administrator)
su -c "python scifferpack.py" # Termux (after gaining root)
