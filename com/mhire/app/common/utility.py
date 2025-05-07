import uuid

def generate_request_id(key):
    request_id = f"REQ-{uuid.uuid5(uuid.NAMESPACE_DNS, key)}"
    return request_id