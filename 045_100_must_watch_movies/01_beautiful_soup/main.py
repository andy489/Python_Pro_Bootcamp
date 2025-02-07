from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

# soup = BeautifulSoup(contents, "lxml")
soup = BeautifulSoup(contents, "html.parser")
# print(type(soup))
# print(soup.title) # title tag
# print(soup.title.name) # title tag name
# print(soup.title.string) # title tag text
# print(soup.li)

all_anchor_tags = soup.find_all(name="a")
all_anchor_tags_texts = [tag.getText() for tag in all_anchor_tags]
all_anchor_tags_hrefs = [tag.get("href") for tag in all_anchor_tags]

# print(all_anchor_tags)
# print(all_anchor_tags_texts)
# print(all_anchor_tags_hrefs)

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")
# print(name)

elements_with_heading_class = soup.select(selector=".heading")
# print(elements_with_heading_class)

# print(soup.prettify())
