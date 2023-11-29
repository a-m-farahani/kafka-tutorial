import requests
import json

PROTO = """
syntax = "proto3";
message Measurement {
    string id = 1;
    int64 timestamp = 2;
    double value = 3;
    uint32 quality = 4;
}
"""

payload = {
    "schemaType": "PROTOBUF",
    "schema": PROTO
    }

response = requests.post("http://localhost:8081/subjects/sensors/versions", data=json.dumps(payload))
# response = requests.delete("http://localhost:8081/subjects/sensors/versions") # delete schema
if response.ok:
    print("schema registered successfully!")
else:
    print("failed to register schema.")