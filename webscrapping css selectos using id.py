#https://www.youtube.com/watch?v=UgiymkXulPY&list=PLGKQkV4guDKEKZXAyeLQZjE6fulXHW11y&index=6
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.marketwatch.com')
soup = BeautifulSoup(response.content, 'html.parser')


# como period represa a class, para id é #hashtag simbol
#<ul id="nav__menu" class="list list--menu j-list">
print(soup.select('ul#nav__menu'))