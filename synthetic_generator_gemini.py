import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


# Prompt template
MIKROTIK_PROMPT_TEMPLATE = """Generate detailed technical MikroTik RouterOS documentation for the following scenario. Include practical examples, configurations, and explanations.

Context:
- Focus on RouterOS {version} (6.x or 7.x)
- Configuration Level: {level} (Basic/Advanced/Expert)
- Network Scale: {scale} (SOHO/SMB/Enterprise/ISP)

Topic: {topic}

Required components:
1. Configuration scenario and requirements
2. Step-by-step implementation
3. Complete configuration commands
4. Common pitfalls and solutions
5. Verification and testing steps
6. Related features and considerations

Format the output in clean markdown with:
- Clear section headers
- Code blocks for commands
- Bullet points for steps
- Tables for parameters
- Notes for important warnings

Special Instructions:
- Focus on practical, real-world implementations
- Include error handling and troubleshooting
- Provide command syntax with parameter explanations
- Add security best practices where relevant
"""

TOPIC_CATEGORIES = {
    "Networking": [
        "VLAN Configuration",
        "Bridge Setup",
        "Layer3 Routing",
        "MPLS Implementation",
        "QoS and Queue Management"
    ],
    "Security": [
        "Firewall Rule Design",
        "NAT Configuration",
        "VPN Setup",
        "Access Control Lists",
        "Certificate Management"
    ],
    "Automation": [
        "REST API Usage",
        "Script Development",
        "Scheduled Tasks",
        "Custom Tools",
        "Automated Backups"
    ],
    "Advanced": [
        "BGP Configuration",
        "OSPF Setup",
        "MPLS VPN",
        "Traffic Engineering",
        "High Availability"
    ]
}

SCENARIOS = {
    "Network_Scale": ["SOHO", "SMB", "Enterprise", "ISP"],
    "Complexity": ["Basic", "Advanced", "Expert"],
    "RouterOS_Version": ["6.48", "7.11", "7.12"]
}


def generate_mikrotik_documentation(topic, version, level, scale):
    """Generates MikroTik documentation for a specific scenario."""
    prompt = MIKROTIK_PROMPT_TEMPLATE.format(
        topic=topic, version=version, level=level, scale=scale
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating content for topic '{topic}', version '{version}', level '{level}', scale '{scale}': {e}")
        return None

def format_filename(topic, version, level, scale):
        """Formats a filename based on the scenario."""
        safe_topic = topic.replace(" ", "_").replace("/", "_")
        return f"{safe_topic}_{version}_{level}_{scale}.md"

def save_to_markdown(output, filename, output_dir="C:\\Users\\Vivek\\Documents\\MikroTik_dis\\Scraped_Data\\synthetic_data"):
        """Saves the generated output to a Markdown file."""
        output_dir_path = Path(output_dir)
        output_dir_path.mkdir(parents=True, exist_ok=True)
        file_path = output_dir_path / filename

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving to file {file_path}: {e}")

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
                             time.sleep(2)
                             
if __name__ == "__main__":
     main()