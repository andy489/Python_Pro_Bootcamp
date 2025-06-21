import requests
from bs4 import BeautifulSoup

SCRAPPING_URL = "https://news.ycombinator.com/"

response = requests.get(SCRAPPING_URL)
response.raise_for_status()

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles_titles = soup.select(selector="span.titleline > a")
article_upvotes = soup.find_all(name="span", class_="score")

result = [(anchor.getText(), anchor.get("href"), int(article_upvotes[i].getText().split()[0]))
          for i, anchor in enumerate(articles_titles)]

# Sort by upvotes (third element in tuple) in descending order
sorted_result = sorted(result, key=lambda x: x[2], reverse=True)

# Print the sorted results
for item in sorted_result:
    print(f"Upvotes: {item[2]} | Title: {item[0]} | URL: {item[1]}")

print("Highest Rated Article:")
print(sorted_result[0])
