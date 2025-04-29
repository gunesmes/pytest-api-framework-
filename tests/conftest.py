# File: /testing-framework/testing-framework/tests/conftest.py

import pytest
from src.config import ENVIRONMENTS, ENV

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default=ENV,
        help="Specify the environment to run tests against: dev, staging, prod"
    )

@pytest.fixture(scope="session")
def environment(request):
    env_name = request.config.getoption("--env")
    if env_name not in ENVIRONMENTS:
        raise ValueError(f"Unknown environment: {env_name}. Available environments: {', '.join(ENVIRONMENTS.keys())}")
    return ENVIRONMENTS[env_name]

@pytest.fixture
def api_client(environment):
    print(f" - Creating API client for {environment['base_url']}")
    from src.api_client import ApiClient
    return ApiClient(base_url=environment["base_url"])