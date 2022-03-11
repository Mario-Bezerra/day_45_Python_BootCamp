import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
all_titles_texts = [tittle.getText() for tittle in all_titles]

all_titles_texts_in_order = all_titles_texts[::-1]

with open("movies_list.txt", "w") as data:
    for tittle in all_titles_texts_in_order:
        data.write(f"{tittle}\n")

