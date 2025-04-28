import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        print(response)
        return self._handle_response(response)

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        return self._handle_response(response)

    def put(self, endpoint, data=None):
        response = requests.put(f"{self.base_url}{endpoint}", json=data)
        return self._handle_response(response)

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code in range(200, 300):
            return response
        else:
            response.raise_for_status()