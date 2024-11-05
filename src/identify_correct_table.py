import requests
from bs4 import BeautifulSoup
import os

def print_all_tables(html, file=None):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    
    output = []
    output.append(f"Found {len(tables)} tables.")
    
    for idx, table in enumerate(tables):
        output.append(f"\nTable {idx + 1} HTML snippet:")
        output.append(table.prettify()[:5000])  # Show the first 5000 characters for review
    
    if file:
        with open(file, 'w', encoding='utf-8') as f:
            f.write("\n".join(output))
    else:
        print("\n".join(output))

if __name__ == "__main__":
    url = "https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia"
    headers = {
        'User-Agent': 'MyScriptBot/1.0 (contact@example.com)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP status codes 4xx/5xx
        html = response.text
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        exit()

    # Define the path for the output file
    output_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'html_tables_result.txt')
    
    # Ensure the 'data' directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    print_all_tables(html, file=output_file_path)
