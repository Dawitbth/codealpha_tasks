# Important libraries and packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

# URL to Scrape
base_url = 'https://books.toscrape.com/'

def scrape_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to access:", url)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_='product_pod')

    results = []

    for book in books:
        title = book.h3.a['title']

        price = book.select_one(".price_color").get_text(strip=True)

        rating = book.select_one(".star-rating")["class"][1]
        availability = book.find('p', class_='instock').text.strip()
        relative_url = book.h3.a['href']
        product_url = urljoin(url, relative_url)
# Store the reuslts
        results.append({
                
            "Title" : title,
            "Price" : price,
            "Rating" : rating,
            "Availability" : availability,
            "URL" : product_url            
        })
    return results

all_books = []

for page in range(1,51):
    if page ==1:
        url = base_url
    else:
        url = urljoin(
            base_url,
            f"catalogue/page-{page}.html"
        )
    print(f"Scraping Page {page}...")

    page_data = scrape_page(url)

    if not page_data:
        print("No more data found.")
        break

    all_books.extend(page_data)

    time.sleep(1)

print("Total books Collected: ", len(all_books))

# Create DataFrame
df = pd.DataFrame(all_books)

# Adjust the price column
df['Price'] = (df["Price"]
              .str.replace("Â£", "", regex=False)
              .astype(float))

# Convert ratings

rating_map = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5
}
df["Rating "] = df["Rating"].map(rating_map)

# Drop the original Rating column
df = df.drop(columns=['Rating'])

# Save the final dataset
df.to_csv(
    "scraped_books_dataset.csv",
    index=False
)
print("scraped_books_dataset.csv Successfully Saved!")

