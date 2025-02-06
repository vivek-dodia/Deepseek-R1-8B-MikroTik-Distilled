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
        """Flatten a list of parameter dictionaries into a JSON string.

        This function takes a list of parameter dictionaries, extracts relevant
        fields such as 'name', 'in', and 'type' from each parameter, and returns
        a JSON string representation of the flattened parameters. If the input
        list is empty, it returns an empty JSON array.

        Args:
            params (List[dict]): A list of dictionaries representing parameters,
                each containing 'name', 'in', and 'schema' fields.

        Returns:
            str: A JSON string representation of the flattened parameters.
        """

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
        """Flatten the request body for a JSON schema.

        This function takes a request body dictionary and extracts the relevant
        properties from the 'content' section, specifically for the
        'application/json' media type. If the body is empty or does not contain
        'content', it returns a default structure indicating that no properties
        are required. Otherwise, it retrieves the properties from the schema and
        returns them in a flattened format.

        Args:
            body (Dict): A dictionary representing the request body, which may
                contain 'content' and 'required' fields.

        Returns:
            Dict: A dictionary containing 'required' status and 'properties'
                as a JSON string.
        """

        if not body or 'content' not in body:
            return {'required': False, 'properties': '{}'}
        
        properties = body.get('content', {}).get('application/json', {}).get('schema', {}).get('properties', {})
        return {
            'required': body.get('required', False),
            'properties': json.dumps(properties)
        }

    def flatten_responses(self, responses: Dict) -> Dict:
        """Flatten a dictionary of responses into a simplified structure.

        This function takes a dictionary of responses, extracts relevant
        information, and returns a flattened version of the responses. Each
        response is represented by its code, and the flattened structure
        includes the description and type of each response. The output is a JSON
        string representation of the flattened responses.

        Args:
            responses (Dict): A dictionary where each key is a response code and each
                value is a dictionary containing response details.

        Returns:
            str: A JSON string representing the flattened responses.
        """

        flat_responses = {}
        for code, details in responses.items():
            flat_responses[code] = {
                'description': details.get('description', ''),
                'type': details.get('content', {}).get('application/json', {}).get('schema', {}).get('type', '')
            }
        return json.dumps(flat_responses)

    def extract_endpoints(self) -> List[Dict[str, Any]]:
        """Extract endpoints from the OpenAPI specification.

        This method retrieves all endpoints defined in the OpenAPI
        specification. It iterates through the paths and methods, collecting
        relevant details such as the path, HTTP method, operation ID,
        parameters, request body requirements, request properties, and
        responses. The collected information is structured into a list of
        dictionaries, each representing an endpoint.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing details about each endpoint.
        """

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
        """Save extracted endpoints to a JSON Lines file.

        This function retrieves a list of endpoints using the
        `extract_endpoints` method and writes each endpoint to a specified JSON
        Lines file. It handles any exceptions that may occur during the file
        writing process and prints an error message if an error occurs. After
        successfully writing the endpoints, it prints the number of processed
        endpoints.

        Args:
            output_path (str): The file path where the JSON Lines file will be saved.
        """

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