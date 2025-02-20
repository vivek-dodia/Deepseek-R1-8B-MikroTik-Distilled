import os
import logging
import time
from pathlib import Path
from openai import OpenAI, APITimeoutError
import requests
from requests.auth import HTTPBasicAuth
from urllib3.util import ssl_
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv

ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
load_dotenv()

API_KEY = os.getenv("DEEPSEEK")
BASE_DIR = Path("C:/Users/Vivek/Documents/MikroTik_dis/Scraped_Data/synthetic_data/deepseek")
LOG_DIR = Path("C:/Users/Vivek/Documents/MikroTik_dis/logs")
LOG_FILE = LOG_DIR / "deepseek.log"

# Configuration
SCALES = ["SOHO"]  # Start with just SOHO for testing
LEVELS = ["Basic"]  # Start with just Basic
VERSIONS = ["6.x"]  # Start with just 6.x
MAX_RETRIES = 5
TIMEOUT = 60
BATCH_SIZE = 3

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

PROMPT_TEMPLATE = """Generate concise MikroTik RouterOS documentation for:
Topic: {topic}
RouterOS: {version}
Scale: {scale}
Level: {level}

Include:
1. CLI configuration with comments
2. REST API example (Python)
3. Common debugging steps
4. Security measures
5. Performance tips

Format:
- Use Markdown
- Keep CLI examples practical
- Include error handling in API code
"""

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=4, max=30),
    retry=retry_if_exception_type((APITimeoutError, requests.exceptions.Timeout))
)
def generate_completion(client, prompt, topic):
    try:
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a MikroTik expert. Provide practical documentation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7,
            timeout=TIMEOUT
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"API error for topic {topic}: {str(e)}")
        raise

def process_topic_batch(client, batch, scale, level, version):
    results = []
    for topic in batch:
        try:
            prompt = PROMPT_TEMPLATE.format(
                topic=topic,
                version=version,
                level=level,
                scale=scale
            )
            
            filename = f"{scale}_{level}_{version}_{topic.replace(' ','_')}.md"
            filepath = BASE_DIR / filename
            
            if filepath.exists():
                logging.info(f"Skipping existing file: {filename}")
                continue

            content = generate_completion(client, prompt, topic)
            enhanced_content = add_technical_enhancements(content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(enhanced_content)
            
            logging.info(f"Successfully generated: {filename}")
            print(f"Generated: {filename}")
            
            results.append((topic, True))
            time.sleep(5)  # Rate limiting between files
            
        except Exception as e:
            logging.error(f"Failed to generate {topic}: {str(e)}")
            results.append((topic, False))
            time.sleep(2)
            
    return results

def generate_documentation():
    if not API_KEY:
        raise ValueError("Missing DEEPSEEK API key in .env file")

    BASE_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    client = OpenAI(
        api_key=API_KEY,
        base_url="https://api.deepseek.com/v1",
        timeout=TIMEOUT
    )

    while True:
        try:
            for version in VERSIONS:
                for level in LEVELS:
                    for scale in SCALES:
                        for category, topics in EXTENDED_TOPICS.items():
                            # Process topics in batches
                            for i in range(0, len(topics), BATCH_SIZE):
                                batch = topics[i:i + BATCH_SIZE]
                                results = process_topic_batch(client, batch, scale, level, version)
                                
                                # If all failed in batch, wait longer
                                if all(not success for _, success in results):
                                    logging.warning("Batch completely failed, waiting 60 seconds...")
                                    time.sleep(60)
                                else:
                                    time.sleep(10)  # Normal batch delay
            
            logging.info("Completed full cycle, waiting before next iteration")
            time.sleep(30)
            
        except KeyboardInterrupt:
            logging.info("Process interrupted by user")
            break
        except Exception as e:
            logging.error(f"Critical error: {str(e)}")
            time.sleep(60)

def add_technical_enhancements(content):
    api_helper = """\n\n## API Helper Class
```python
class MikrotikAPI:
    def __init__(self, router_ip: str, api_user: str, api_pass: str, verify_ssl: bool = False):
        self.base_url = f"https://{router_ip}/rest"
        self.auth = HTTPBasicAuth(api_user, api_pass)
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.timeout = 30
    
    def api_call(self, method: str, endpoint: str, data: dict = None):
        try:
            response = self.session.request(
                method,
                f"{self.base_url}{endpoint}",
                auth=self.auth,
                json=data,
                verify=self.verify_ssl,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {str(e)}"}
```\n"""
    return content + api_helper

if __name__ == "__main__":
    try:
        generate_documentation()
    except Exception as e:
        logging.error(f"Application terminated: {str(e)}")
    finally:
        logging.info("Documentation generation completed")