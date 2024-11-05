# Public Holiday Parser

| Author | Date | Version | Description |
|--------|------|---------|-------------|
| Marcos Paricio | 2024/08/09 | 0.0.1 | Document creation |

This project aims to extract and process public holiday data for Western Australia for the years 2024 and 2025 from a webpage. The extracted data is stored in an in-memory SQLite database and verified using unit tests.

[TOC]

## Project Overview

### Task 2: Detect & Parse Holidays

**Objective:** Extract information about holidays for the years 2024 and 2025 from the webpage [Public Holidays Western Australia](https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia).

**Functionality:**

1. **Data Extraction:** Uses the `requests` library to fetch the HTML content and `BeautifulSoup` to parse it.
2. **Data Parsing:** Identifies and extracts relevant information about public holidays, including:
   - **Year**
   - **Holiday Date**
   - **Holiday Name**
3. **Data Display:** Prints the extracted data in a formatted table in the console.

**Folder:** `src`
**File:** `main.py`
**Run command:** `make run` (Note: Use make run from the project root directory to execute the main.py script without needing to change directories)

### Task 3: Implement Unit Tests

**Objective:** Implement unit tests for the `parse_holidays` function to ensure correctness.

**Folder:** `tests`
**File:** `test_parser.py`
**Run command:** `make test` (Note: Use make test from the project root directory to run tests without needing to change directories)

**Tests Included:**

- **`test_parse_holidays`**: Validates that the `parse_holidays` function correctly parses the provided HTML and extracts the expected data.

### Task 4: Save Data to SQLite and Verify

**Objective:** Save the parsed holiday data into an in-memory SQLite database and verify the correct storage.

**Functionality:**

1. **Save to SQLite:** Uses `SQLAlchemy` to create and interact with an in-memory SQLite database.
2. **Data Retrieval:** Queries the database to retrieve and print the stored holiday data.

### ***Auxiliary Script***
identify_correct_table.py

**Purpose**: Identifies and examines HTML tables from the webpage. This script helps in determining which table to use in main.py by:

1. **Fetching HTML Content**: Makes an HTTP GET request to the provided URL.
2. **Parsing HTML**: Finds and lists all tables using BeautifulSoup.
3. **Displaying Tables**: Prints out snippets of each table's HTML for review, which aids in identifying the correct table based on its structure and content.

**Folder:** `src`
**File:** `identity_correct_table.py`
**Run command:** make html_tables` (Note: Use make html_tables from the project root directory to run identify_correct_table without needing to change directories)