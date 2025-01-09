# %%
import os
import base64
import requests
from dotenv import load_dotenv

# %%
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')

load_dotenv(os.path.join(BASE_DIR, '.env'))
url = os.getenv('POWER_AUTOMATE_URL')

# File path from the file that will be send
file_path = os.path.join(BASE_DIR, 'data/MySampleFile.xlsx')

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} was not found.")

# Read the file content and encode to Base64
with open(file_path, "rb") as file:
    file_content = base64.b64encode(file.read()).decode()

# %%
# Prepare the HTTP request payload
payload = {
    "fileName": os.path.basename(file_path),
    "fileContent": {
        "$content-type": "application/octet-stream",
        "$content": file_content #File content in base64
    }
}

# Set the request headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request to Power Automate
# response = requests.post(url, json=payload, headers=headers, verify=False)
response = requests.post(url, json=payload, headers=headers)

# Process the response
if response.status_code == 200:
    print(f"File '{os.path.basename(file_path)}' uploaded successfully!")
else:
    print(f"Failed to upload the file. Status code: {response.status_code}")
    print(f"Response details: {response.text}")

# %%