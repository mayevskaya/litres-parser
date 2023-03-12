from bs4 import BeautifulSoup
from pymongo import MongoClient
from fake_useragent import UserAgent
import requests, json, fake_proxy

# Collect data from main page of Litres.ru
def get():

  ua = UserAgent(browsers=["edge", "chrome"])
  header = {
    "user-agent": ua.random,
    "accept": "accept: application/json, text/plain, */*"
  }

  url = "https://litres.ru/"

  response = requests.get(url, header, proxies=fake_proxy.get())

  # Create local file and save raw html into it
  open('litres.html', 'w').write(response.text)
  

# Sort gotten information
def sort():

  raw = open('litres.html', 'r')
  soup = BeautifulSoup(raw, 'lxml')
  
  # Get all the div-wrappers of links
  books = soup.find_all('div', class_="Art-module__bookInfo_2CrYb")
  # Then, get all the links
  links = [link.find('a')['href'] for link in books]

  # Fortunately, we can get names of books and its authors by classes
  names = [i.text for i in soup.find_all(class_="Art-module__name__row_2S_Yp")]
  authors = [i.text for i in soup.find_all(class_="Art-module__author_1QaFB")]

  return names, authors

# Extract information to JSON
def extract(names, authors):
  data = [{"Name": names[i], "Author": authors[i]} for i in range(len(names)
    )]
  open('data.json', 'w').write(f'{json.dumps(data, ensure_ascii=False)}')

if __name__ == '__main__':
  get()
  names, authors = sort()
  extract(names, authors)
  print("Succesfully! `data.json` and `litres.html` appeared in this directory.")