import pandas as pd
from src.config import FILE_PATHS  # Import JSON-based config

class WeatherTransformer:
    def __init__(self):
        """Initialize with column names from config.json (if needed)."""
        self.columns = {
            "temperature": "temperature",
            "humidity": "humidity",
            "wind_speed": "wind_speed",
            "weather_desc": "weather_descriptions",
            "property_name": "property_name",
            "city": "city"
        }

    def convert_temperature(self, df):
        """Convert temperature from Celsius to Fahrenheit."""
        df["temperature_F"] = df[self.columns["temperature"]] * 9/5 + 32
        return df

    def categorize_wind(self, df):
        """Categorize wind speed into Low, Moderate, and High."""
        def categorize(speed):
            if speed < 5:
                return "Low"
            elif 5 <= speed < 15:
                return "Moderate"
            else:
                return "High"

        df["wind_category"] = df[self.columns["wind_speed"]].apply(categorize)
        return df

    def normalize_humidity(self, df):
        """Normalize humidity (Scale between 0-1)."""
        df["humidity_normalized"] = df[self.columns["humidity"]] / 100
        return df

    def categorize_weather(self, df):
        """Categorize weather descriptions."""
        def categorize(desc):
            if "Sunny" in desc:
                return "Clear"
            elif "Cloud" in desc or "Haze" in desc:
                return "Cloudy"
            elif "Rain" in desc:
                return "Rainy"
            else:
                return "Other"

        df["weather_category"] = df[self.columns["weather_desc"]].apply(categorize)
        return df

    def melt_data(self, df):
        """Convert wide format to long format (Pivot)."""
        return df.melt(
            id_vars=[self.columns["property_name"], self.columns["city"]], 
            value_vars=[self.columns["temperature"], self.columns["humidity"], self.columns["wind_speed"]],
            var_name="weather_metric", value_name="value"
        )
