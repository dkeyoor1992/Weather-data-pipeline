# Weather-data-pipeline
This project automates the process of fetching real-time weather data from an API, transforming it for analysis, and storing it in an AWS S3 bucket.


# 🌦️ Weather Data Pipeline - Fetch, Transform & Store in AWS S3 🚀

📌 Overview
This project automates the process of fetching real-time weather data from an API, transforming it for analysis, and storing it in an AWS S3 bucket.

---

## ✨ Features
✅ Fetches real-time weather data for multiple locations using an API  
✅ Transforms and processes data for meaningful insights  
✅ Converts temperature to Fahrenheit, categorizes wind speed & normalizes humidity  
✅ Stores the final processed data in **AWS S3**  
✅ Fully **modular design** following **OOP best practices**  
✅ Configurations managed using a **JSON file** for flexibility  

---

## 📂 Folder Structure
weather_data_pipeline/ 
├── src/ 
│ ├── fetch_weather.py
│ ├── transform.py 
│ ├── s3_uploader.py 
│ ├── config.py
├── config.json
├── main.py
├── requirements.txt
├── README.md

** 2 Create a Virtual Environment **
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

** 3. Install Dependencies**
pip install -r requirements.txt

🚀 Usage

1️⃣ Fetch Weather Data from API
python main.py

2️⃣ Upload Transformed Data to AWS S3
The script automatically uploads the processed file to AWS S3. Ensure you have correct AWS permissions.

3️⃣ Verify Data in S3
Go to AWS S3 Console → Navigate to your bucket → Check for weather_data_transformed.csv.

📊 Data Transformations
Temperature Conversion: Celsius → Fahrenheit
Wind Speed Categorization: Low / Moderate / High
Humidity Normalization: Scaled between 0-1
Weather Categorization: Clear, Cloudy, Rainy, etc.
Melt Operation: Converts wide format to long format


🔒 Security Best Practices
✅ Do NOT hardcode API keys in Python scripts
✅ Use config.json to store sensitive credentials
✅ Grant IAM permissions with least privilege (e.g., only s3:PutObject)
✅ Use .gitignore to prevent uploading credentials

📌 Future Improvements
🔄 Automate scheduling with Airflow or Lambda
📊 Connect Tableau / Power BI for dashboard insights
🏎️ Optimize with multi-threading for faster API requests
🔄 Store data in AWS Glue / Athena for queries


📜 License
This project doesn't need a License.








