import os
import pandas as pd
import requests


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

# Assuming 'data' is a list of dictionaries, convert it into a DataFrame
df = pd.DataFrame(data)

# Define the expected schema
expected_schema = {
    # Add or modify the schema according to your specific requirements and data structure
    'stat_Year': 'int64',
    'stateName': 'object',
    'reportName': 'object',
    'farmType': 'object',
    'category': 'object',
    'categoryValue': 'object',
    'category2': 'object',
    'category2Value': 'object',
    'variableId': 'object',
    'variableName': 'object',
    'variableSequence': 'int64',
    'variableLevel': 'int64',
    'variableGroup': 'object',
    'variableGroupId': 'object',
    'variableUnit': 'object',
    'variableDesc': 'object',
    'variableIsInValid': 'bool',
    'estimate': 'float64',
    'median': 'float64',
    'statistic': 'object',
    'rse': 'float64',
    'unreliable_Est': 'int64',
    'dec_Disp': 'int64',
    'series': 'object',
    'serie_Dim': 'object',
    'series2': 'object',
    'serie2_Dim': 'object',
    'series_Element': 'object',
    'serie_Element_Dim': 'object',
    'series2_Element': 'object',
    'serie2_Element_Dim': 'object',
    'fips_St': 'int64',
    'survey_Abb': 'object',
    'survey_Dim': 'object',
    'subject_Num': 'int64',
    'subject_Dim': 'object',
    'topic_Abb': 'object',
    'variable': 'object',
    'topic_Dim': 'object',
    'report_Num': 'int64',
    'report_Dim': 'object',
    'state': 'object',
}

# Convert columns to the expected data type
for column, dtype in expected_schema.items():
    if column in df.columns:
        try:
            df[column] = df[column].astype(dtype)
        except ValueError as e:
            print(f"Error converting column {column} to {dtype}: {e}")
    else:
        print(f"Column missing in the DataFrame: {column}")

# Check for missing columns
missing_columns = set(expected_schema.keys()) - set(df.columns)
if missing_columns:
    print(f"Missing columns in the DataFrame: {missing_columns}")

print("Schema validation and API data fetch completed.")
