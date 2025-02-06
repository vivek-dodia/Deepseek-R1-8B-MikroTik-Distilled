import yaml
import json
import os
from typing import Dict, List, Any
import jsonlines

class APISpecProcessor:
    def __init__(self, yaml_path: str):
        self.yaml_path = yaml_path
        with open(yaml_path, 'r', encoding='utf-8') as f:
            self.spec = yaml.safe_load(f)

    def flatten_parameters(self, params: List) -> str:
        if not params:
            return "[]"
        flat_params = []
        for p in params:
            flat_param = {
                'name': p.get('name', ''),
                'in': p.get('in', ''),
                'type': p.get('schema', {}).get('type', '')
            }
            flat_params.append(flat_param)
        return json.dumps(flat_params)

    def flatten_request_body(self, body: Dict) -> Dict:
        if not body or 'content' not in body:
            return {'required': False, 'properties': '{}'}
        
        properties = body.get('content', {}).get('application/json', {}).get('schema', {}).get('properties', {})
        return {
            'required': body.get('required', False),
            'properties': json.dumps(properties)
        }

    def flatten_responses(self, responses: Dict) -> Dict:
        flat_responses = {}
        for code, details in responses.items():
            flat_responses[code] = {
                'description': details.get('description', ''),
                'type': details.get('content', {}).get('application/json', {}).get('schema', {}).get('type', '')
            }
        return json.dumps(flat_responses)

    def extract_endpoints(self) -> List[Dict[str, Any]]:
        endpoints = []
        paths = self.spec.get('paths', {})
        
        for path, methods in paths.items():
            for method, details in methods.items():
                if isinstance(details, dict):
                    endpoint = {
                        'path': path,
                        'method': method.upper(),
                        'operation_id': details.get('operationId', ''),
                        'parameters': self.flatten_parameters(details.get('parameters', [])),
                        'request_body_required': self.flatten_request_body(details.get('requestBody', {}))['required'],
                        'request_properties': self.flatten_request_body(details.get('requestBody', {}))['properties'],
                        'responses': self.flatten_responses(details.get('responses', {}))
                    }
                    endpoints.append(endpoint)
        return endpoints

    def save_jsonl(self, output_path: str):
        try:
            endpoints = self.extract_endpoints()
            with jsonlines.open(output_path, mode='w') as writer:
                for endpoint in endpoints:
                    writer.write(endpoint)
            print(f"Processed {len(endpoints)} endpoints")
        except Exception as e:
            print(f"Error saving JSONL: {str(e)}")

if __name__ == "__main__":
    input_path = r"C:\Users\Vivek\Documents\MikroTik_dis\openapi\7.13.5.yaml"
    output_dir = r"C:\Users\Vivek\Documents\MikroTik_dis\parquet_data\openapi"
    output_path = os.path.join(output_dir, "mikrotik_api_flat.jsonl")
    
    os.makedirs(output_dir, exist_ok=True)
    processor = APISpecProcessor(input_path)
    processor.save_jsonl(output_path)