import pandas as pd
from src.fetch_weather import WeatherFetcher
from src.transform import WeatherTransformer
from src.s3_uploader import S3Uploader
from src.config import FILE_PATHS

# Load dataset
df = pd.read_csv(FILE_PATHS["input_csv"])

# Fetch weather data
weather_fetcher = WeatherFetcher()
df_weather = weather_fetcher.fetch_weather(df)

# Apply transformations
transformer = WeatherTransformer()
df_melted = transformer.melt_data(df_weather)

# Save transformed file
df_melted.to_csv(FILE_PATHS["transformed_csv"], index=False)

# Upload to S3
s3_uploader = S3Uploader()
s3_uploader.upload_df_to_s3(df_melted)

print("Pipeline execution complete!")
