PET_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "category": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "required": ["id", "name"]
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": [{"type": "string"}]
        },
        "tags": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                    "required": ["id", "name"]
                }
            ]
        },
        "status": {
            "type": "string"
        }
    },
    "required": ["id", "name", "photoUrls", "tags", "status"]
}

PETS_ARRAY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "category": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    },
                    "required": ["id", "name"]
                },
                "name": {"type": "string"},
                "photoUrls": {
                    "type": "array",
                    "items": [{"type": ["string", "null"]}]
                },
                "tags": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "name": {"type": "string"}
                            },
                            "required": ["id", "name"]
                        }
                    ]
                },
                "status": {"type": "string"}
            },
            "required": ["id", "name", "status"]
        }
    ]
}

ORDER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "items": {}
        },
        "tags": {
            "type": "array",
            "items": {}
        },
        "status": {"type": "string"}
    },
    "required": ["id", "name", "photoUrls", "tags", "status"]
}

INVENTORY_SCHEMA = {
    "type": "object",
    "additionalProperties": {"type": "integer", "minimum": 0}
}

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string"},
        "phone": {"type": "string"},
        "userStatus": {"type": "integer"}
    },
    "required": ["id", "username", "email"]
}

SUCCESS_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    },
    "required": ["code", "type"]
}