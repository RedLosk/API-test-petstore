import jsonschema
import pytest
from jsonschema import validate

def validate_schema(response_json, schema):
    #Validate JSON response against schema
    validate(instance=response_json, schema=schema)

def validate_response_time(response, max_time=5):
    #Validate response time is within limit
    elapsed = response.elapsed.total_seconds()
    assert elapsed < max_time

def validate_content_type(response, expected_type="application/json"):
    #Validate Content-Type header
    content_type = response.headers.get("Content-Type", "")
    assert expected_type in content_type

def validate_http_code(response, expected_code):
    #Validate HTTP status code
    assert response.status_code == expected_code