import json

def validate_json(data):
    """
    Validate the JSON structure. Add more checks as needed.
    """
    required_keys = ["timestamp", "event_name", "payload"]
    if not all(key in data for key in required_keys):
        raise ValueError("Invalid JSON format!")
    return True