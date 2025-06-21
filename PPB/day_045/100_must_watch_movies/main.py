import requests
from bs4 import BeautifulSoup

SCRAPPING_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(SCRAPPING_URL)
response.raise_for_status()

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())

all_movies = soup.select(selector="div > span > h2 > strong")
# print(all_movies)

movie_titles = [tag.getText() for tag in all_movies]
# for n in range(len(movie_titles) - 1, -1, -1):
#     print(movie_titles[n])
movies_reversed = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies_reversed:
        file.write(f"{movie}\n")