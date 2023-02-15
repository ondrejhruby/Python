import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
response = requests.get("https://www.calistfitness.com/")

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the products listed on the website
products = soup.find_all('div', class_='product')

# Open a CSV file for writing and write header row
with open('calistfitness_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product', 'Price', 'Rating'])

    # Loop through each product and extract the relevant information
    for product in products:
        name = product.find('h3', class_='product-title').text.strip()
        price = product.find('div', class_='price').text.strip()
        rating = product.find('span', class_='stars').text.strip()
        
        # Write the data to the CSV file
        writer.writerow([name, price, rating])
