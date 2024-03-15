import os
import pandas as pd
import requests
import uuid
from datetime import datetime

# Function to fetch data from the API
def fetch_data_from_api(api_key, url, method='GET', payload=None):
    try:
        if method == 'GET':
            response = requests.get(url, params=payload)
        elif method == 'POST':
            response = requests.post(url, json=payload)
        else:
            raise ValueError("Unsupported HTTP method. Use GET or POST.")
        
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

# Define API key and URL using environmental variables
api_key = os.getenv('USDA_API_KEY')
url_template = "https://api.ers.usda.gov/data/arms/surveydata"

if not api_key:
    raise ValueError("API key is missing. Please set the environmental variable USDA_API_KEY.")

# Generate payload for the API request
payload = {
    "year": [2011, 2012, 2013, 2014, 2015, 2016],
    "state": "all",
    "variable": "igcfi",
    "category": "NASS Regions",
    "category2": "Collapsed Farm Typology"
}

# Call the API and process the data
data = fetch_data_from_api(api_key, url_template, method='POST', payload=payload)
print("Data fetched from API:", data)  # Debug statement

# Check if the API response contains data
if 'data' not in data or not data['data']:
    print("No data found in the API response.")
    exit()

# Assuming 'data' is a list of dictionaries, convert it into a DataFrame
try:
    df = pd.DataFrame(data['data'])
    print("DataFrame created successfully.")
except Exception as e:
    print("Error creating DataFrame:", e)  # Debug statement
    raise  # Reraise exception for detailed traceback

# Generate unique identifier
unique_id = uuid.uuid4()

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Save the DataFrame to a CSV file with unique name
output_file_name = f"usda_arms_survey_data_{current_date}_{unique_id}.csv"
output_file_path = os.path.join("usda_food_arms/data", output_file_name)
df.to_csv(output_file_path, index=False)
print(f"DataFrame saved to {output_file_path}")
