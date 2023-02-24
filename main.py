from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

# Operating data, provider role. Body of application
class Main:
  pass

# Getting data, service role. Skeleton of application
class Func:

  def get_data():

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
    
Func.get_data()