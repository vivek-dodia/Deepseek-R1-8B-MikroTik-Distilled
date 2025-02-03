import os
import logging
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import time
from requests.auth import HTTPBasicAuth
from urllib3.util import ssl_
ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

load_dotenv()
API_KEY = os.getenv("DEEPSEEK")

BASE_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\Scraped_Data\synthetic_data\deepseek"
LOG_DIR = r"C:\Users\Vivek\Documents\MikroTik_dis\logs"
LOG_FILE = Path(LOG_DIR) / "deepseek.log"

SCALES = ["SOHO", "SMB", "Enterprise", "ISP"]
LEVELS = ["Basic", "Advanced", "Expert"]
VERSIONS = ["6.x", "7.x"]

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

# Configure logging
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_documentation():
    Path(BASE_DIR).mkdir(parents=True, exist_ok=True)

    if not API_KEY:
        print("Missing DEEPSEEK in .env file")
        exit(1)
    
    try:
        client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com/v1")
    except Exception as e:
        print(f"Failed to initialize the deepseek client: {str(e)}")
        exit(1)
    
    while True: # Recursive Loop
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
                                command_response = client.chat.completions.create(
                                    model="deepseek-chat",
                                    messages=[{
                                        "role": "system",
                                        "content": "You are a MikroTik Certified Engineer. Provide expert documentation with CLI/API examples and technical diagrams."
                                    }, {
                                        "role": "user",
                                        "content": prompt
                                    }],
                                    max_tokens=2000, # Adjusted tokens here if needed
                                    temperature=0.1,
                                    stream=False,
                                    timeout=60 # Added timeout
                                )
                                
                                content = command_response.choices[0].message.content
                                enhanced_content = add_technical_enhancements(content)
                                
                                with open(filepath, 'w', encoding='utf-8') as f:
                                    f.write(enhanced_content)
                                print(f"Generated: {filename}")
                            
                            except Exception as e:
                                logging.error(f"Error generating {filename}: {str(e)}")
                                if hasattr(e,'response'):
                                    logging.error(f"Response Content: {e.response.content.decode()}")
                                print(f"Error generating {filename}: {str(e)}")
        print("All Topics Done, Sleeping for 10 seconds")
        time.sleep(10)

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
```\n"""
    return content + enhancements

if __name__ == "__main__":
    try:
      generate_documentation()
    except KeyboardInterrupt:
        print("Documentation generation interrupted by user.")
    print("Documentation generation completed!")