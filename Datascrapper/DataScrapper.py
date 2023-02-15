import csv
import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://www.octoparse.com/"
page = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(page.content, "html.parser")

# Find the data you want to extract
data = soup.find_all("tag_name", {"class_name": "class_value"})

# Store the extracted data in a list
rows = []
for item in data:
    rows.append([item.text])

# Write the data to a CSV file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
