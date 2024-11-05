import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
import pandas as pd
import re

def clean_text(text):
    """
    Removes special characters and extra spaces from text.
    """
    if text is None:
        return ""
    text = text.strip()
    text = text.replace('*', '(special date)').replace('#', '(special holiday)')  # Remove special characters
    text = ' '.join(text.split())  # Remove extra spaces
    return text

def parse_holidays(html):
    """
    Parses the HTML to extract holiday information for the years 2024 and 2025.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Find the appropriate table by other characteristics, in this case the summary
    holiday_table = soup.find('table', {'summary': 'A table listing the public holiday dates for 2020, 2021 and 2022.'})

    if not holiday_table:
        raise Exception("No holiday table found in the HTML.")
    
    # Extract the years from the column headers
    headers = holiday_table.find_all('th')
    if len(headers) < 4:
        raise Exception("Expected table headers not found.")
    years = [header.get_text(strip=True) for header in headers[1:]]  # Extract years from column headers

    rows = holiday_table.find_all('tr')[1:]  # Skip the header row
    if not rows:
        raise Exception("No rows found in the holiday table.")

    holidays = []
    for row in rows:
        cols = row.find_all('td')
        if not cols:
            continue  # Skip rows without columns

        # The holiday name is in the first column
        holiday_name_cell = row.find('th')
        if not holiday_name_cell:
            raise Exception("Holiday name cell not found in row.")
        holiday_name = clean_text(holiday_name_cell.get_text(strip=True))

        # Process the dates
        for i, col in enumerate(cols):
            date_info = clean_text(col.get_text(strip=True).replace('\xa0', ' '))
            if date_info:
                year = years[i]  # Get the year corresponding to the index
                if year not in ['2024', '2025']:
                    continue  # Only process the years 2024 and 2025 como dice en el pdf que me ha mandado Lucia
                dates = date_info.split('&')
                for date in dates:
                    date = clean_text(date.strip())
                    if date:
                        holiday = {
                            "Year": year,
                            "Holiday Date": date,
                            "Holiday Name": holiday_name
                        }
                        holidays.append(holiday)

    return holidays

def extract_date_parts(date_str):
    """
    Extracts day and month from a date string.
    Assumes the format is like "Monday 1 January" or "Friday 29 March".
    """
    match = re.match(r"(\w+)\s(\d+)\s(\w+)", date_str)
    if match:
        day_name, day, month = match.groups()
        return (int(day), month)
    return (0, "")

def save_to_sqlite(holidays):
    """
    Saves the holidays data to an SQLite database and prints it in a pretty format.
    """
    engine = create_engine('sqlite:///:memory:') # an in-memory SQLite database
    metadata = MetaData()

    holidays_table = Table('holidays', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('Year', String),
                           Column('Holiday Date', String),
                           Column('Holiday Name', String)
    )
    metadata.create_all(engine) # creates the table in the database

    conn = engine.connect()
    conn.execute(holidays_table.insert(), holidays)

    # Read and display the data using pandas for better visualization
    query = holidays_table.select()
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

    # Drop the 'id' column
    df = df.drop(columns=['id'])

    # Convert 'Holiday Date' to a sortable format
    df[['Day', 'Month']] = df['Holiday Date'].apply(lambda x: pd.Series(extract_date_parts(x)))
    df['Date'] = pd.to_datetime(df['Month'] + ' ' + df['Day'].astype(str) + ', ' + df['Year'], format='%B %d, %Y', errors='coerce')

    # Sort DataFrame by 'Year' and 'Date'
    df = df.sort_values(by=['Year', 'Date']).reset_index(drop=True)

    # Drop temporary columns
    df = df.drop(columns=['Day', 'Month', 'Date'])

    # Pretty print DataFrame with improved alignment
    print("\nPublic holidays in Western Australia - 2024 and 2025\n")
    
    # Calculate column widths for better alignment
    col_widths = {
        "Holiday Name": max(df["Holiday Name"].apply(len).max(), len("Holiday Name")),
        "Year": max(df["Year"].apply(len).max(), len("Year")),
        "Holiday Date": max(df["Holiday Date"].apply(len).max(), len("Holiday Date"))
    }
    
    # Adjust space between columns
    spacing = 15  # Increase spacing between columns

    # Print header with left alignment
    header = (
        f"{'Holiday Name'.ljust(col_widths['Holiday Name'] + spacing)}"
        f"{'Year'.ljust(col_widths['Year'] + spacing)}"
        f"{'Holiday Date'.ljust(col_widths['Holiday Date'])}"
    )
    print(header)
    
    # Print separator line
    separator = (
        f"{'-' * (col_widths['Holiday Name'] + spacing)}"
        f"{'-' * (col_widths['Year'] + spacing)}"
        f"{'-' * col_widths['Holiday Date']}"
    )
    print(separator)
    
    # Print rows
    for _, row in df.iterrows():
        print(
            f"{str(row['Holiday Name']).ljust(col_widths['Holiday Name'] + spacing)}"
            f"{str(row['Year']).ljust(col_widths['Year'] + spacing)}"
            f"{str(row['Holiday Date']).ljust(col_widths['Holiday Date'])}"
        )
    print("\n")

if __name__ == "__main__":
    url = "https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia"
    headers = {
        'User-Agent': 'MyScriptBot/1.0 (marcos.paricio.mp@gmail.com)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP status codes 4xx/5xx
        html = response.text
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {e}")
        exit()

    try:
        holidays = parse_holidays(html)
        save_to_sqlite(holidays)
    except Exception as e:
        print(f"Error during processing: {e}")
