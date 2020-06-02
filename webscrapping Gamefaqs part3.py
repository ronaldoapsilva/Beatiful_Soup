import requests
from bs4 import BeautifulSoup

response = requests.get('https://gamefaqs.gamespot.com/', headers = {'User-Agent': 'Mozilla/5.0'})
#print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")