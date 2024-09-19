import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save(url, filename):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming the product info is in 'product' divs with name, price, and rating classes
    products = [{'Product Name': p.find('span', class_='product-name').text.strip(),
                 'Price': p.find('span', class_='price').text.strip(),
                 'Rating': p.find('div', class_='rating').text.strip() if p.find('div', class_='rating') else 'No Rating'}
                for p in soup.find_all('div', class_='product')]

    # Save data to CSV
    pd.DataFrame(products).to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage
url = 'https://example-ecommerce-website.com/category/products'  # Replace with actual URL
scrape_and_save(url, 'product_data.csv')
