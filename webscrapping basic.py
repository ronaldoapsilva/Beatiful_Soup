#https://www.youtube.com/watch?v=2egPL5KFCC8&list=PLGKQkV4guDKEKZXAyeLQZjE6fulXHW11y&index=2
#java scrip cannot be pull by beautifulsoap, java scrip use sileniun
#resultdo 0 para atributo existentem, vem exemplo imagem como pegar
import requests
from bs4 import BeautifulSoup
url = "https://www.marketwatch.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
soup.find_all('div', class_ = "element element--latestNews")
#print(len(soup.find_all('div', class_ = "element element--latestNews"))) #sempre usar len para sabe quantos elementos/tag tem, neste caso o elemento/tag é div, para sabe quantidade div com o mesmo nome, vemos qual é o atributo, neste caso é uma class, se fosse um atributo id, não precisa de sabe quantas div, pois id são unicos, com class nome "element element--latestNews" temos apenas len = 1
#print(soup.find_all('div', class_ = "element element--latestNews"))


def linkes():
    print(soup.find('a').get('href'))
#HTML links are defined with the <a> tag. The link address is specified in the href attribute: no caso acima extrai apenas um link, para extrair todo usar um loop
#linkes()

def listas():
    print(soup.find_all('ul'))
    print(5*'\n')
    print(len(soup.find_all('ul')))
    print(5*'\n')
    print(soup.find_all('ul')[0])
    print(5*'\n')
    print(soup.find_all('ul', class_ ="list list--menu j-list"))
    print(len(soup.find_all('ul', class_ ="list list--menu j-list")))
    print(5*'\n')
#https://www.w3schools.com/html/html_lists.asp
#https://www.youtube.com/watch?v=5IxadAxTS04&list=PLGKQkV4guDKEKZXAyeLQZjE6fulXHW11y&index=3
#listas()


def imagem():
    #print(soup.find_all('img'))
    print(soup.find('img').get('src'))
    print(soup.find('img').get('data-src')) #get nao funciona para o atributo 'data-src', usa o codigo abaixo, 
    print(soup.find('img', attrs = {'data-src' : True}))
    #print(soup.findAll('img', attrs = {'data-src' : True}))
#https://www.w3schools.com/html/html_images.asp
imagem()