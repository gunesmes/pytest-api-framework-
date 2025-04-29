"""Configuration settings for the API testing framework."""

# Environment-specific configurations
import os


ENVIRONMENTS = {
    "prod": {
        "base_url": "https://poetrydb.org",
        "timeout": 5
    },
    "staging": {
        "base_url": "https://staging.poetrydb.org",
        "timeout": 10
    },
    "dev": {
        "base_url": "https://dev.poetrydb.org",
        "timeout": 10
    }
}

# Default environment
ENV = "prod"

# Validate environment
if ENV not in ENVIRONMENTS:
    raise ValueError(f"Invalid environment: {ENV}. Available environments: {', '.join(ENVIRONMENTS.keys())}")

# API configuration that dynamically uses the base_url from the selected environment
API_CONFIG = {
    "base_url": ENVIRONMENTS[ENV]["base_url"],
    "timeout": ENVIRONMENTS[ENV]["timeout"],
    "retry_attempts": 3
}