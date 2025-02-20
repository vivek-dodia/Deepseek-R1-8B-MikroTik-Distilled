import os
import logging
import random
import ipaddress
import uuid
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
import time
from requests.auth import HTTPBasicAuth
from urllib3.util import ssl_
ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

# Load environment variables and configure Gemini API
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

BASE_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\synthetic_data\gemini2.0FlashThinking"
LOG_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\logs"
LOG_FILE = Path(LOG_DIR) / "gemini.log"

SCALES = ["SOHO", "SMB", "Enterprise", "ISP"]
LEVELS = ["Basic", "Advanced", "Expert"]
VERSIONS = ["7.x"]

EXTENDED_TOPICS = {
    "Core Networking": [
        "IP Addressing (IPv4 and IPv6)",
        "IP Pools",
        "IP Routing",
        "IP Settings",
    ],
    "Access Control": [
        "MAC server",
        "RoMON",
        "WinBox",
    ],
    "Security Services": [
      "Certificates",
      "PPP AAA",
      "RADIUS",
      "User / User groups",
    ],
    "Bridging & Switching": [
        "Bridging and Switching",
        "MACVLAN",
        "L3 Hardware Offloading",
        "MACsec",
        "VLAN",
        "VXLAN",
    ],
    "Firewall & QoS": [
        "Firewall and Quality of Service",
        "Connection tracking",
        "Firewall",
        "Packet Flow in RouterOS",
        "Queues",
        "Firewall and QoS Case Studies",
        "Kid Control",
        "UPnP",
        "NAT-PMP",
    ],
    "IP Services":[
        "IP Services"
    ],
    "High Availability": [
         "High Availability Solutions",
        "Load Balancing",
        "Bonding",
        "Bonding Examples",
        "HA Case Studies",
        "Multi-chassis Link Aggregation Group",
        "VRRP",
        "VRRP Configuration Examples",
    ],
    "Mobile Networking": [
      "Mobile Networking",
        "GPS",
        "LTE",
        "PPP",
        "SMS",
        "Dual SIM Application",
    ],
    "MPLS": [
      "Multi Protocol Label Switching - MPLS",
        "MPLS Overview",
        "MPLS MTU, Forwarding and Label Bindings",
        "EXP bit and MPLS Queuing",
        "LDP",
        "VPLS",
        "Traffic Eng",
        "MPLS Reference",
    ],
    "Network Management": [
        "Network Management",
        "ARP",
        "Cloud",
        "DHCP",
        "DNS",
        "SOCKS",
        "Proxy",
        "Openflow",
    ],
    "Routing": [
        "Routing",
        "Routing Protocol Overview",
        "Moving from ROSv6 to v7 with examples",
        "Routing Protocol Multi-core Support",
        "Policy Routing",
        "Virtual Routing and Forwarding - VRF",
        "OSPF",
        "RIP",
        "BGP",
        "RPKI",
        "Route Selection and Filters",
         "Multicast",
        "Routing Debugging Tools",
         "Routing Reference",
          "BFD",
           "IS-IS",
    ],
    "System Information": [
         "System Information and Utilities",
        "Clock",
         "Device-mode",
        "E-mail",
        "Fetch",
        "Files",
         "Identity",
        "Interface Lists",
        "Neighbor discovery",
        "Note",
        "NTP",
        "Partitions",
        "Precision Time Protocol",
         "Scheduler",
        "Services",
        "TFTP",
    ],
    "Virtual Private Networks": [
        "Virtual Private Networks",
        "6to4",
         "EoIP",
        "GRE",
        "IPIP",
         "IPsec",
         "L2TP",
       "OpenVPN",
        "PPPoE",
        "PPTP",
       "SSTP",
       "WireGuard",
       "ZeroTier",
    ],
    "Wired Connections": [
        "Wired Connections",
        "Ethernet",
         "MikroTik wired interface compatibility",
         "PWR Line"
    ],
    "Wireless": [
        "Wireless",
        "WiFi",
        "Wireless Interface",
        "W60G",
        "CAPsMAN",
         "HWMPplus mesh",
          "Nv2",
         "Interworking Profiles",
         "Wireless Case Studies",
        "Spectral scan",
    ],
    "Internet of Things": [
         "Internet of Things",
       "Bluetooth",
       "GPIO",
       "Lora",
      "MQTT"
    ],
    "Hardware":[
        "Hardware",
        "Disks",
        "Grounding",
        "LCD Touchscreen",
        "LEDs",
        "MTU in RouterOS",
        "Peripherals",
        "PoE-Out",
        "Ports",
        "Product Naming",
        "RouterBOARD",
        "USB Features",
    ],
    "Diagnostics": [
        "Diagnostics, monitoring and troubleshooting",
        "Bandwidth Test",
        "Detect Internet",
        "Dynamic DNS",
        "Graphing",
        "Health",
        "Interface stats and monitor-traffic",
        "IP Scan",
        "Log",
        "Netwatch",
        "Packet Sniffer",
        "Ping",
        "Profiler",
        "Resource",
        "SNMP",
        "Speed Test",
        "S-RJ10 general guidance",
        "Torch",
        "Traceroute",
        "Traffic Flow",
        "Traffic Generator",
        "Watchdog",
    ],
    "Extended Features":[
        "Extended features",
        "Container",
        "DLNA Media server",
        "ROSE-storage",
        "SMB",
        "UPS",
        "Wake on LAN",
        "IP packing"
    ]
}

PROMPT_TEMPLATE = """Generate comprehensive MikroTik RouterOS documentation with CLI and API examples for:

**Topic:** {topic}
**RouterOS Version:** {version}
**Network Scale:** {scale}
**Complexity Level:** {level}

Include these components:
1. Architecture diagram requirements
2. CLI configuration with inline comments
3. REST API implementation (Python code)
4. Common debugging scenarios
5. Version-specific considerations
6. Security hardening measures
7. Performance optimization tips

Special requirements for {scale} environments:
- Include real-world deployment examples
- Show scalability considerations
- Provide monitoring configurations
- Add disaster recovery steps
- Include automated backup scripts

Format requirements:
- Use Markdown with technical notation
- Commands in RouterOS code blocks
- API examples in Python with error handling
- Network diagrams in mermaid syntax
- Comparative tables for different approaches
"""

def generate_documentation():
    Path(BASE_DIR).mkdir(parents=True, exist_ok=True)

    if not GOOGLE_API_KEY:
        print("Missing GOOGLE_API_KEY in .env file")
        exit(1)
    
    try:
        # Initialize Gemini model with the specified config
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 65536,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            generation_config=generation_config,
        )
        
        print("Successfully initialized Gemini model")
    except Exception as e:
        print(f"Failed to initialize the Gemini client: {str(e)}")
        exit(1)
    
    while True:
        for version in VERSIONS:
            for level in LEVELS:
                for scale in SCALES:
                    for category, topics in EXTENDED_TOPICS.items():
                        for topic in topics:
                            prompt = PROMPT_TEMPLATE.format(
                                topic=topic,
                                version=version,
                                level=level,
                                scale=scale
                            )
                            
                            filename = f"{scale}_{level}_{version}_{topic.replace(' ','_')}.md"
                            filepath = Path(BASE_DIR) / filename
                            
                            try:
                                print(f"\nGenerating documentation for {topic}...")
                                
                                # Create chat session for better context
                                chat = model.start_chat(history=[])
                                
                                # First message: System prompt
                                system_message = "You are a MikroTik Certified Engineer providing detailed documentation with CLI/API examples and technical diagrams."
                                chat.send_message(system_message)
                                
                                # Second message: Main prompt
                                response = chat.send_message(prompt)
                                
                                if not response.text:
                                    raise ValueError("Empty response received from Gemini API")
                                
                                content = response.text
                                enhanced_content = add_technical_enhancements(content)
                                
                                # Add metadata
                                metadata = f"""---
generated_at: {datetime.now().isoformat()}
topic: {topic}
category: {category}
version: {version}
scale: {scale}
level: {level}
model: gemini-2.0-flash-thinking-exp-01-21
---

"""
                                full_content = metadata + enhanced_content
                                
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(full_content)
                                    
                                print(f"Generated: {filename}")
                                print(f"Content length: {len(full_content)} bytes")
                                logging.info(f"Successfully generated {filename}")
                                
                            except Exception as e:
                                error_msg = f"Error generating {filename}: {str(e)}"
                                logging.error(error_msg)
                                print(error_msg)
                            
                            # Add delay between requests
                            time.sleep(10)
                            
        print("\nAll topics generated. Sleeping for 120 seconds before next cycle...")
        time.sleep(120)

def add_technical_enhancements(content):
    enhancements = """\n\n## API Reference Cheat Sheet
```python
# Universal API Helper Function
def mikrotik_api_call(
    method: str,
    endpoint: str,
    data: dict = None,
    timeout: int = 10
) -> dict:
    '''
    Universal MikroTik API handler with error checking
    '''
    try:
        response = requests.request(
            method,
            f"https://{ROUTER_IP}/rest{endpoint}",
            auth=HTTPBasicAuth(API_USER, API_PASS),
            json=data,
            verify=SSL_VERIFY,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code} - {e.response.text}")
        return {"error": str(e)}
```"""
    return content + enhancements

if __name__ == "__main__":
    # Configure logging
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        generate_documentation()
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    except Exception as e:
        print(f"\nScript error: {str(e)}")
        logging.error(f"Script error: {str(e)}")
    finally:
        print("Script execution completed!")