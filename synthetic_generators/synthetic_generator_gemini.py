import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time
from datetime import datetime
import logging
import random
import ipaddress

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
- Target RouterOS {version} (6.48, 7.x).
- Configuration Level: {level} (Basic/Advanced/Expert)
- Network Scale: {scale} (SOHO, SMB, Enterprise, ISP, Hotspot Network, Point-to-Point Link).
- Provide a specific configuration for the following parameters:
    - Subnet: {random_subnet}
    - Interface Name: {random_interface}

Topic: {topic}

Instructions:
- {instruction_wording}

## Scenario Description:
Provide a clear and concise description of the scenario being addressed.

## Implementation Steps:
Provide a step-by-step guide, explain each step and why it is needed. Provide examples of CLI or winbox GUI instructions, before *and* after each configuration step and the effect each step is supposed to have. The output should be very specific, actionable and complete.
1. **Step 1**: ...
2. **Step 2**: ...
...

## Complete Configuration Commands:
Provide a complete set of MikroTik CLI commands to implement the setup, including a full explanation for each parameter.

## Common Pitfalls and Solutions:
Outline common problems that may arise from this configuration. Also suggest methods to diagnose and fix these problems. If there are potential security or configuration issues, be sure to highlight these. Include information for potential resource issues, such as high CPU or memory usage.

## Verification and Testing Steps:
Provide detailed steps on how to verify this configuration is working as expected. Include specific MikroTik tools (ping, traceroute, torch, etc.).

## Related Features and Considerations:
Discuss any other relevant MikroTik features or considerations that could be used in combination with the current setup. Explain the impact of the current configuration in the real world scenarios.

## MikroTik REST API Examples (if applicable):
Provide clear, executable REST API examples if applicable including API endpoint, request method, example JSON payload, and the expected response. Ensure these examples use MikroTik specific API calls, and provide a complete description of each parameter. If an error can arise from an api call, describe how to handle it.

## Security Best Practices
Outline key security best practices for this configuration, specifically for less common features.

## Self Critique and Improvements
Critique this configuration. What can be improved, or further modified to make it better?

## Detailed Explanations of Topic
Provide clear and detailed information on the given topic.

## Detailed Explanation of Trade-offs
Explain the trade-offs between using different configurations and settings, especially for more complex features.

## Configuration for Specific RouterOS Versions:
If targeting a specific RouterOS version, instruct the model to only use commands relevant to that version.

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
- Ensure all examples are tested and verifiable.
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
       "Multi-WAN Failover with Load Balancing",
        "Complex VPN Tunneling (IPsec or WireGuard)",
        "Advanced QoS with HTB and PCQ",
        "BGP with Multiple Upstream Providers",
       "MPLS L3 VPN",
        "Hotspot with RADIUS Authentication and Custom Branding",
        "Centralized Logging and Monitoring",
        "Advanced Firewall with Layer 7 Filtering",
       "Dynamic DNS with Scripting",
        "High Availability (HA) with VRRP",
   ]
}

SCENARIOS = {
    "Network_Scale": ["SOHO", "SMB", "Enterprise", "ISP", "Hotspot Network", "Point-to-Point Link"],
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


def generate_random_subnet():
    """Generates a random /24 IPv4 subnet."""
    base_ip = str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))
    network = ipaddress.IPv4Network(f"{base_ip}/24", strict=False)
    return str(network)

def generate_random_interface():
        """Generates a random interface name."""
        prefixes = ["ether", "wlan", "vlan", "bridge"]
        suffix = random.randint(0, 99)
        return f"{random.choice(prefixes)}-{suffix}"

def generate_instruction_wording():
        """Generates a different instruction wording."""
        wordings = [
           "Create a detailed, step-by-step example",
           "Implement a practical solution",
           "Provide a clear configuration example",
           "Show how to configure this feature",
           "Demonstrate a working implementation"
        ]
        return random.choice(wordings)

def generate_mikrotik_documentation(topic, version, level, scale):
    """Generates MikroTik documentation for a specific scenario."""
    random_subnet = generate_random_subnet()
    random_interface = generate_random_interface()
    instruction_wording = generate_instruction_wording()
    prompt = MIKROTIK_PROMPT_TEMPLATE.format(
        topic=topic,
        version=version,
        level=level,
        scale=scale,
        random_subnet=random_subnet,
        random_interface=random_interface,
        instruction_wording=instruction_wording,
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