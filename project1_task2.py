import requests
from bs4 import BeautifulSoup

myres = requests.get("https://www.orionscache.com/books")
soup = BeautifulSoup(myres.text, "html.parser")
print(soup)
