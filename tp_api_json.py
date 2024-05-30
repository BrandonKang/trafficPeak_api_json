from requests.auth import HTTPBasicAuth
import requests
import json
import argparse
import os

# Set constants for URL
API_URL = os.getenv('API_URL')

# Read credentials from environment variables
USERNAME = os.getenv('API_USERNAME')
PASSWORD = os.getenv('API_PASSWORD')

def execute_query(query):
    if USERNAME is None or PASSWORD is None:
        print("Error: API credentials are not set in the environment variables.")
        return

    # Extract column names from the query
    columns = [col.strip().split()[-1] for col in query.split("SELECT")[1].split("FROM")[0].split(",")]

    # Make data request
    response = requests.post(API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), data=query)

    # Convert response data to JSON format
    if response.status_code == 200:
        lines = response.text.strip().split('\n')

        result = []

        # Parse data and convert to JSON
        for line in lines:
            values = line.split('\t')
            record = dict(zip(columns, values))
            result.append(record)

        # Output JSON data
        json_data = json.dumps(result, indent=4, ensure_ascii=False)
        print(json_data)
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute a SQL query and get the result in JSON format.")
    parser.add_argument("query", type=str, help="The SQL query to execute")

    args = parser.parse_args()
    execute_query(args.query)