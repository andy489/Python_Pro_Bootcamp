from bs4 import BeautifulSoup

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://www.linkedin.com/robots.txt

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p.prettify()) # first p tag

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    curr_link = tag.get("href")
    print(curr_link)

web_technologies_skills = soup.find(id="web-tech")
print(web_technologies_skills)

# organizations_i_have_worked_for = soup.find_all(name="div", attrs={"class": "company-name"})
organizations_i_have_worked_for = soup.find_all(name="div", class_="company-name")
print(organizations_i_have_worked_for)

curr_company_name = soup.select_one(selector="div.company-name")
print(curr_company_name.string)
