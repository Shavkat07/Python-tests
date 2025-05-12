import requests
from bs4 import BeautifulSoup

# Choose any URL
url = "https://habr.com/ru/companies/otus/articles/901130/"  # Replace with any site you want

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad status codes

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Get the page title
    print("Page Title:", soup.title.string)

    # Find all <a> tags (links)
    print("\nAll Links:")
    for text in soup.find_all("p"):
        # href = link.get("href")
        content = text
        if content:
            print(content)

except requests.exceptions.RequestException as e:
    print("Error accessing the site:", e)
