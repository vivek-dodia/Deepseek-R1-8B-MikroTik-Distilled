import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time
from datetime import datetime
import logging

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Using Gemini 2.0 Flash Experimental
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")


# Updated Prompt template for enhanced MikroTik knowledge
MIKROTIK_PROMPT_TEMPLATE = """As a highly experienced MikroTik RouterOS expert, generate detailed technical documentation for the following scenario. Include practical examples, configurations, and explanations with a strong focus on MikroTik-specific commands and concepts.

Context:
- Target RouterOS {version} (6.x or 7.x)
- Configuration Level: {level} (Basic/Advanced/Expert)
- Network Scale: {scale} (SOHO/SMB/Enterprise/ISP)

Topic: {topic}

Required components:
1. Comprehensive configuration scenario and specific MikroTik requirements.
2. Step-by-step MikroTik implementation using CLI or Winbox with detailed explanations.
3. Complete MikroTik CLI configuration commands with relevant parameters.
4. Common MikroTik-specific pitfalls, troubleshooting, and diagnostics using built-in tools.
5. Verification and testing steps using MikroTik tools (ping, traceroute, torch, etc.).
6. Related MikroTik-specific features, capabilities, and limitations.
7. MikroTik REST API examples (if applicable), including API endpoint, request method, example JSON payload, and expected response. Ensure these examples use MikroTik specific API calls.
8. In-depth explanations of core concepts, focusing on MikroTik's implementation (e.g., bridging, routing, firewall).
9. Security best practices specific to MikroTik routers.
10. Detailed explanations and configuration examples for the following MikroTik topics:

   - IP Addressing (IPv4 and IPv6)
   - IP Pools
   - IP Routing
   - IP Settings
   - MAC server
   - RoMON
   - WinBox
   - Certificates
   - PPP AAA
   - RADIUS
   - User / User groups
   - Bridging and Switching
   - MACVLAN
   - L3 Hardware Offloading
   - MACsec
   - Quality of Service
   - Switch Chip Features
   - VLAN
   - VXLAN
   - Firewall and Quality of Service (Including: Connection tracking, Firewall, Packet Flow in RouterOS, Queues, Firewall and QoS Case Studies, Kid Control, UPnP, NAT-PMP)
   - IP Services (DHCP, DNS, SOCKS, Proxy)
   - High Availability Solutions (Including: Load Balancing, Bonding, Bonding Examples, HA Case Studies, Multi-chassis Link Aggregation Group, VRRP, VRRP Configuration Examples)
   - Mobile Networking (Including: GPS, LTE, PPP, SMS, Dual SIM Application)
   - Multi Protocol Label Switching - MPLS (Including: MPLS Overview, MPLS MTU, Forwarding and Label Bindings, EXP bit and MPLS Queuing, LDP, VPLS, Traffic Eng, MPLS Reference)
   - Network Management (Including: ARP, Cloud, DHCP, DNS, SOCKS, Proxy, Openflow)
   - Routing (Including: Routing Protocol Overview, Moving from ROSv6 to v7 with examples, Routing Protocol Multi-core Support, Policy Routing, Virtual Routing and Forwarding - VRF, OSPF, RIP, BGP, RPKI, Route Selection and Filters, Multicast, Routing Debugging Tools, Routing Reference, BFD, IS-IS)
   - System Information and Utilities (Including: Clock, Device-mode, E-mail, Fetch, Files, Identity, Interface Lists, Neighbor discovery, Note, NTP, Partitions, Precision Time Protocol, Scheduler, Services, TFTP)
   - Virtual Private Networks (Including: 6to4, EoIP, GRE, IPIP, IPsec, L2TP, OpenVPN, PPPoE, PPTP, SSTP, WireGuard, ZeroTier)
   - Wired Connections (Including: Ethernet, MikroTik wired interface compatibility, PWR Line)
   - Wireless (Including: WiFi, Wireless Interface, W60G, CAPsMAN, HWMPplus mesh, Nv2, Interworking Profiles, Wireless Case Studies, Spectral scan)
    - Internet of Things (Including: Bluetooth, GPIO, Lora, MQTT)
    - Hardware (Including: Disks, Grounding, LCD Touchscreen, LEDs, MTU in RouterOS, Peripherals, PoE-Out, Ports, Product Naming, RouterBOARD, USB Features)
    - Diagnostics, monitoring and troubleshooting (Including: Bandwidth Test, Detect Internet, Dynamic DNS, Graphing, Health, Interface stats and monitor-traffic, IP Scan, Log, Netwatch, Packet Sniffer, Ping, Profiler, Resource, SNMP, Speed Test, S-RJ10 general guidance, Torch, Traceroute, Traffic Flow, Traffic Generator, Watchdog)
    - Extended features (Including: Container, DLNA Media server, ROSE-storage, SMB, UPS, Wake on LAN, IP packing)


Format the output in clean markdown with:
- Clear section headers
- Code blocks for MikroTik CLI commands.
- Bullet points for steps.
- Tables for parameters.
- Notes for important MikroTik warnings and considerations.
- Code blocks for REST API examples.

Special Instructions:
- Focus on practical, real-world MikroTik implementations.
- Include error handling and troubleshooting that are specific to MikroTik devices.
- Provide MikroTik command syntax with detailed parameter explanations.
- Add security best practices relevant to MikroTik routers.
- Provide clear, executable examples with API calls, requests, and responses.
- Provide examples of CLI usage via MikroTik's Winbox GUI, where relevant.
"""

TOPIC_CATEGORIES = {
    "All_Topics": [
       "IP Addressing (IPv4 and IPv6)",
       "IP Pools",
       "IP Routing",
        "IP Settings",
       "MAC server",
       "RoMON",
       "WinBox",
       "Certificates",
       "PPP AAA",
        "RADIUS",
        "User / User groups",
       "Bridging and Switching",
       "MACVLAN",
        "L3 Hardware Offloading",
       "MACsec",
       "Quality of Service",
       "Switch Chip Features",
       "VLAN",
       "VXLAN",
       "Firewall and Quality of Service",
       "IP Services",
       "High Availability Solutions",
       "Mobile Networking",
       "Multi Protocol Label Switching - MPLS",
       "Network Management",
       "Routing",
       "System Information and Utilities",
        "Virtual Private Networks",
       "Wired Connections",
       "Wireless",
       "Internet of Things",
       "Hardware",
        "Diagnostics, monitoring and troubleshooting",
        "Extended features",
    ]
}

SCENARIOS = {
    "Network_Scale": ["SOHO", "SMB", "Enterprise", "ISP"],
    "Complexity": ["Basic", "Advanced", "Expert"],
    "RouterOS_Version": ["6.48", "7.11", "7.12"]
}

# Setup logging
LOG_DIR = Path("C:\\Users\\Vivek\\Documents\\MikroTik_dis\\logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "gemini.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def generate_mikrotik_documentation(topic, version, level, scale):
    """Generates MikroTik documentation for a specific scenario."""
    prompt = MIKROTIK_PROMPT_TEMPLATE.format(
        topic=topic, version=version, level=level, scale=scale
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error generating content for topic '{topic}', version '{version}', level '{level}', scale '{scale}': {e}")
        return None


def format_filename(topic, version, level, scale):
    """Formats a filename based on the scenario."""
    safe_topic = topic.replace(" ", "_").replace("/", "_")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Adds a timestamp
    return f"{safe_topic}_{version}_{level}_{scale}_{timestamp}.md"


def save_to_markdown(output, filename, output_dir="Scraped_Data\\synthetic_data\\gemini2.0"):
    """Saves the generated output to a Markdown file."""
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)
    file_path = output_dir_path / filename

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output)
        logging.info(f"Successfully saved to {file_path}")
        print(f"Successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving to file {file_path}: {e}")


def main():
    """Main function to iterate through scenarios and generate data."""
    for category, topics in TOPIC_CATEGORIES.items():
        for topic in topics:
            for version in SCENARIOS["RouterOS_Version"]:
                for level in SCENARIOS["Complexity"]:
                    for scale in SCENARIOS["Network_Scale"]:

                        output = generate_mikrotik_documentation(topic, version, level, scale)
                        if output:
                            filename = format_filename(topic, version, level, scale)
                            save_to_markdown(output, filename)
                            logging.info(f"Generated file: {filename}, Topic: {topic}, Version: {version}, Level: {level}, Scale: {scale}")
                            time.sleep(2)


if __name__ == "__main__":
    main()