from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 ("
                         ".NET CLR 3.5.30729)"}

work = Session()
work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"csrf_token": "token", "username": "noname", "password": "passw"}

result = work.post("https://quotes.toscrape.com/login", data=data, headers=headers, allow_redirects=True)

res = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")