import requests
import json

SCHEMA = """
{
  "$schema": "",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "value": {
      "type": "number"
    },
    "quality": {
      "type": "integer"
    },
    "timestamp": {
      "type": "integer"
    }
  },
  "required": [
    "id",
    "name",
    "value",
    "quality",
    "timestamp"
  ]
}
"""

data = {
    "schemaType": "JSON",
    "schema": SCHEMA
    }

response = requests.post("http://localhost:8081/subjects/sensors/versions", data=json.dumps(data)) # register schema
# response = requests.delete("http://localhost:8081/subjects/sensors/versions/1") # delete schema

if response.ok:
    print("schema registered successfully!")
else:
    print("failed to register schema.")