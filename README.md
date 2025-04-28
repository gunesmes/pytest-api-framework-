# Testing Framework

This project is a simple testing framework built using Python, pytest, and the requests library. It provides an API client for making HTTP requests and includes utility functions for various tasks.

## Project Structure

```
testing-framework
├── src
│   ├── api_client.py
│   └── utils.py
├── tests
│   ├── conftest.py
│   └── test_api.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd testing-framework
pip install -r requirements.txt
```

## Usage

### ApiClient

The `ApiClient` class in `src/api_client.py` allows you to make HTTP requests. Here are some examples:

```python
from src.api_client import ApiClient

client = ApiClient(base_url="https://api.example.com")

# GET request
response = client.get("/endpoint")
print(response)

# POST request
data = {"key": "value"}
response = client.post("/endpoint", json=data)
print(response)
```

### Utility Functions

The utility functions in `src/utils.py` can be used for tasks such as data validation and response handling.

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

Test result
```bash
(3.10.8) ➜  testing-framework git:(main) pytest
====================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.10.8, pytest-8.3.5, pluggy-1.5.0 -- /Users/mesutgunes/.pyenv/versions/3.10.8/bin/python
cachedir: .pytest_cache
rootdir: /Users/mesutgunes/projects/personal/new-api/testing-framework
configfile: pytest.ini
testpaths: tests
collected 4 items                                                                                                                                                                               

tests/test_api.py::test_list_all_authors_using_author PASSED                                                                                                                              [ 25%]
tests/test_api.py::test_list_all_authors_using_authors PASSED                                                                                                                             [ 50%]
tests/test_api.py::test_search_by_author PASSED                                                                                                                                           [ 75%]
tests/test_api.py::test_search_by_author_return_output_fields_format_as_text PASSED                                                                                                       [100%]

======================================================================================= 4 passed in 3.84s =======================================================================================
```

This will discover and execute all test cases defined in the `tests` directory.

## Test Validation Strategy

The test suite employs several validation approaches to ensure API endpoints function correctly:

### Status Code Validation
Verifies that API endpoints respond with the expected HTTP status codes:
```python
assert response.status_code == 200
```

### Content Presence Validation
```python
assert "Ernest Dowson" in str(response.content)
assert "Emily Dickinson" in str(response.content)
```
These verify that expected author names are present in responses when listing authors.

### Content Absence Validation
These confirm that poems by other authors (like Emily Dickinson) are not included when filtering for a specific author (Dowson).
```python
assert "And the Debate was done." not in str(response.content)
```

### JSON Structure Validation
These ensure the API returns the expected JSON fields, validating the response format.
```python
assert '"title":' in str(response.content)
assert '"author":' in str(response.content)
assert '"lines":' in str(response.content)
```

### Format-Specific Validation
In the last test, this checks that when specifying output fields with the .text format, only the requested fields are returned.
```python
assert "linecount" not in str(response.content)
```

These validations ensure the API behaves as expected across different endpoints and with various query parameters.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.