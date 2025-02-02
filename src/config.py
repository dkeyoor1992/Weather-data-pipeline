import json

# Load config.json file
with open("config.json", "r") as f:
    config = json.load(f)

# Extract values
FILE_PATHS = config["file_paths"]
API_CONFIG = config["api_config"]
AWS_CONFIG = config["aws_config"]
