# File: /testing-framework/testing-framework/tests/conftest.py

import pytest

@pytest.fixture(scope="session")
def api_client():
    from src.api_client import ApiClient
    return ApiClient()