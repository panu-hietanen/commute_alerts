import requests
import os

class WazeClient:
    url = "https://api.openwebninja.com/waze/alerts-and-jams"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = { 'x-api-key': os.getenv('X_API_KEY') }
    
    def get_alerts(self, coords: dict[str, tuple[float, float]]):
        params = self.get_params(coords)
        response = requests.get(self.url, headers=self.headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_params(coords):
       return {
        "top_right":   f"{coords["home"][0]},{coords["home"][1]}",
        "bottom_left": f"{coords["work1"][0]},{coords["work1"][1]}",
        }
        