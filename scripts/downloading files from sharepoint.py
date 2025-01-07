# %%

# Downloading files from Sharepoint with Python + Power Automates

import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
data_path = os.path.join(BASE_DIR, 'data')

url = os.getenv('WORKFLOW_URL')
response = requests.get(url)

binary_content = response.content

# Nome do arquivo de saída
output_file = 'MySampleFile.xlsx'

# Escrevendo os dados binários no arquivo
with open(os.path.join(data_path, output_file), 'wb') as file:
    file.write(binary_content)

print(f"File '{output_file}' created successfully!")

# %%
