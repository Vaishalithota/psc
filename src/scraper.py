import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'http://example.com'

# Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the title of the page
print(soup.title.text)

# Save the title to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    writer.writerow([soup.title.text])

# Modify scraper.py to scrape additional data

    additional_data = soup.find_all('p')

    for data in additional_data:

        writer.writerow([data.text])



# tests/test_scraper.py

import unittest
from unittest.mock import patch, MagicMock
from src.scraper import fetch_data  # Ensure the import path is correct

class TestScraper(unittest.TestCase):

    @patch('src.scraper.requests.get')  # Mock requests.get used in fetch_data
    def test_fetch_data(self, mock_get):
        # Mock response object
        mock_response = MagicMock()
        mock_response.text = '''
        <html>
        <head><title>Example Domain</title></head>
        <body>
        <p>This is a paragraph.</p>
        <p>This is another paragraph.</p>
        </body>
        </html>
        '''
        mock_get.return_value = mock_response

        # Define expected result
        expected_title = "Example Domain"
        expected_additional_data = [
            "This is a paragraph.",
            "This is another paragraph."
        ]
        expected_result = (expected_title, expected_additional_data)

        # Call the function
        result = fetch_data()

        # Assert the result matches expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()