# Data Fetching and Processing

This repository contains scripts for fetching data from the USDA ARMS API, processing it, and saving it to a CSV file.

## Data Fetching

The script pulls data from the USDA ARMS API using a specific API key and URL template, making targeted queries to extract relevant data for analysis.

## Data Processing

Using pandas, the raw data is converted into a DataFrame, facilitating easy manipulation and analysis. Data is validated against an expected schema to ensure correct formatting and types.

## Saving Data

Processed DataFrames are saved to CSV files in the `usda_food_arms/data` directory. Files are uniquely named using the current date and a UUID for easy identification and retrieval.

## Environmental Variables

Set up two environmental variables before running the script:
- `USDA_API_KEY`: Personal key to access the USDA ARMS API.
- `USDA_API_URL_TEMPLATE`: Template URL pointing to the API endpoint.

## Expected Schema

The script expects data to adhere to a predefined structure, specified in the `expected_schema` dictionary, ensuring alignment with anticipated format and types.

## Requirements

Ensure pandas and requests are installed in your Python environment for data manipulation and API data fetching, respectively.

## Usage

1. Set up environmental variables.
2. Run the script to automate the process from data fetching to saving, streamlining your workflow.

## Note

Review and adjust the script as needed, such as modifying the expected schema or API URL template to suit specific requirements.

Work in progress, curiosity/testing/learning for me.
