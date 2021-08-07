import requests
from bs4 import BeautifulSoup

res_info = requests.get("http://127.0.0.1:5500/index.html")

soup = BeautifulSoup(res_info.text)

print("------------HeadLines----------")

for i in range(len(soup)-1):

    print("------HeadLine-----")

    print(soup.find_all("h1")[i].text)

    print("Description Paragraph:")

    print(soup.find_all("p")[i].text)
