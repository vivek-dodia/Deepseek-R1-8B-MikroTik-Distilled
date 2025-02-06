# MikroTik RouterOS REST API Dataset

This dataset contains the complete OpenAPI 2.1 specification for MikroTik RouterOS REST API (v7.13.5) converted to JSONL format for improved querying and analysis.

## Contents
- REST API endpoints
- HTTP methods (GET, POST, PATCH, DELETE)
- Request/response schemas
- Authentication requirements
- Parameter specifications

## Format
- File: `mikrotik_api.jsonl`
- Each line: Complete JSON object representing one API endpoint
- Key fields:
 ```json
 {
   "path": "/endpoint/path", 
   "method": "HTTP_METHOD",
   "operation_id": "OPERATION_ID",
   "parameters": [...],
   "responses": {...},
   "request_body": {...}
 }

 ## Usage

 ```import jsonlines

with jsonlines.open('mikrotik_api.jsonl') as reader:
    for endpoint in reader:
        # Process API endpoint data```