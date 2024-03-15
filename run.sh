#!/bin/bash

# Check if USDA_API_KEY and USDA_API_URL_TEMPLATE environment variables are set
if [ -z "$USDA_API_KEY" ]; then
    echo "Error: USDA_API_KEY environment variable is not set."
    exit 1
fi

if [ -z "$USDA_API_URL_TEMPLATE" ]; then
    echo "Error: USDA_API_URL_TEMPLATE environment variable is not set."
    exit 1
fi

# Run Python script
python usda_arms_survey_data.py
