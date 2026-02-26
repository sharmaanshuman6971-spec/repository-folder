import json

# Step 1: Store JSON-formatted string
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

# Step 2: Parse JSON string into Python dictionary
parsed_response = json.loads(api_response)

# Step 3: Extract values
request_id = parsed_response["id"]
status = parsed_response["status"]
text = parsed_response["result"]["text"]
confidence = parsed_response["result"]["confidence"]

print("Request ID:", request_id)
print("Status:", status)
print("Text:", text)
print("Confidence:", confidence)

# Step 4: Confidence check
if confidence < 0.9:
    print("⚠️ Warning: Confidence score is below threshold!")

# Step 5: Generate JSON
new_response = {
    "id": "req_124",
    "status": "success",
    "result": {
        "text": "Follow-up completed",
        "confidence": 0.95
    }
}

print("\nGenerated JSON:")
print(json.dumps(new_response, indent=4))

# Step 6: Write JSON output to file
with open("response.json", "w") as file:
    file.write(json.dumps(new_response, indent=4))