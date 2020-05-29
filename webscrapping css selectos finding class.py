#https://www.youtube.com/watch?v=UgiymkXulPY&list=PLGKQkV4guDKEKZXAyeLQZjE6fulXHW11y&index=6
import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.marketwatch.com')
soup = BeautifulSoup(page.content, 'html.parser')
#finding all p paragraf
#print(soup.select('p')) 

#finding all div
#print(soup.select('div'))

#finding a tag within tab.... needs to leave a space between them
#print(soup.select("p a"))

#multiple tags
#print(soup.select('p,a'))

'''
Finding Sections by class

need to start with a period to look class name on CSS and the spaces on name needs to completed with period as well
'''
def example1():
    name_1 = 'list list--menu j-list'
    name = name_1.replace(" ", ".")
    #abaixo primeiro print para testar se esta funcionando e o segundo para sabe quantas class com o mesmo nome
    print(soup.select(f".{name}"))
    print(len(soup.select(f".{name}")))
#example1()

def ul_ex():
    #<ul id="nav__menu" class="list list--menu j-list">
    name_1 = 'list list--menu j-list'
    name = name_1.replace(" ", ".")
    # abaixo dois exemplo primeiro css e o segundo beautifulsoup, mesmo resultado o period entre ul e name, significa class
    print(soup.select(f"ul.{name}")) #tag with class - ul tag name
    print(soup.find_all("ul", class_=name_1))
#ul_ex()

def section_ex():
    #<section class="container container--masthead Expanded masthead--expanded">
    name_old1 = 'container container--masthead Expanded masthead--expanded'
    name_new1 = name_old1.replace(" ", ".") #it is to fill space with period
    print(soup.select(f"section.{name_new1}")) #tag with class - section tag name
    print(len(soup.select(f"section.{name_new1}"))) #tag with class - section tag name
#section_ex()

def div_ex():
    #<div class="element element--ad is-loading">
    name_old1 = 'element element--ad is-loading'
    name_new1 = name_old1.replace(" ", ".") #it is to fill space with period
    print(soup.select(f"div.{name_new1}")) #tag with class - section tag name
    print(len(soup.select(f"div.{name_new1}"))) #tag with class - section tag name
div_ex()    
