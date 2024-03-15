import os
import pandas as pd
import requests
import uuid
from datetime import datetime

# Function to fetch data from the API
def fetch_data_from_api(api_key, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

# Define API key and URL using environmental variables
api_key = os.getenv('USDA_API_KEY')
url_template = os.getenv('USDA_API_URL_TEMPLATE')

if not api_key or not url_template:
    raise ValueError("API key or URL template is missing. Please set environmental variables.")

# Generate URL based on template
url = url_template.format(api_key=api_key)

# Call the API and process the data
data = fetch_data_from_api(api_key, url)
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
