from src.config import API_CONFIG
import requests
import pandas as pd

class WeatherFetcher:
    def __init__(self):
        self.api_key = API_CONFIG["weather_api_key"]
        self.url = API_CONFIG["weather_api_url"]

    def fetch_weather(self, df_cities):
        weather_data = []
        
        for _, row in df_cities.iterrows():
            querystring = {"access_key": self.api_key, "query": f"{row['latitude']},{row['longitude']}"}
            response = requests.get(self.url, params=querystring)

            if response.status_code == 200:
                data = response.json()
                if "current" in data:
                    weather_data.append({
                        "property_name": row["property_name"],
                        "city": row["city"],
                        "temperature": data["current"]["temperature"]
                    })
        
        return pd.DataFrame(weather_data)
