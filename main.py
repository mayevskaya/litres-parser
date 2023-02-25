from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

# Collect data from litres
def get():

  ua = UserAgent(browsers=['chrome'])
  header = {
    "user-agent": ua.random,
    "accept": "accept: application/json, text/plain, */*"
  }

  url = "https://litres.ru/"

  response = requests.get(url, header)

  # Create local file and save raw html into it
  raw = open('litres.html', 'w')
  raw.write(response.text)

# Sort gotten information
def sort():

  raw = open('litres.html', 'r')
  soup = BeautifulSoup(raw, 'lxml')
  
  # Get all the div-wrappers of links
  books = soup.find_all('div', class_="Art-module__bookInfo_2CrYb")
  # Then, get all the links
  links = [link.find('a')['href'] for link in books]

  # Fortunately, we can get names of books and its authors by classes
  names = soup.find_all(class_="Art-module__name__row_2S_Yp")
  authors = soup.find_all(class_="Art-module__author_1QaFB")

# Extract information to MongoDB
def extract():
    pass

find_data()