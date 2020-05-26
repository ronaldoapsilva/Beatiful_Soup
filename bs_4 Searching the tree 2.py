html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

def findall():
    print(1, 2*"\n", soup.find_all("title"))
    print(2, "\n", soup.find_all("p", "title"))
    print(3, "\n", soup.find_all("a"))
    print(4, "\n", soup.find_all(id="link2"))

    import re
    print(5, 2*"\n", soup.find(string=re.compile("sisters")))

def argumento():
    print(soup.find_all("title"))
    for tag in soup.find_all("title"):
        print(tag.string)

def keywordarg_1():
    import re
    print(25*'-',1, 25*'-', '\n', soup.find_all(id='link2'))
    print(25*'-',2, 25*'-', '\n', soup.find_all(href=re.compile("elsie")))
    print(25*'-',3, 25*'-', '\n', soup.find_all(id=True))
    for tag in soup.find_all(id=True):
        print(25*'-',4, 25*'-', tag, end = "    |||||||||||||||     ")
    print('\n')
    print(25*'-',5, 25*'-', '\n', soup.find_all(href=re.compile("elsie"), id='link1'))
    
def keywordarg_2():
    data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
    #print(25*'-',6, 25*'-', '\n', data_soup.find_all(data-foo="value"))

def keywordarg_3():
    data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
    print(25*'-',7, 25*'-', '\n', data_soup.find_all(attrs={"data-foo": "value"}))

def keywordarg_4():
    name_soup = BeautifulSoup('<input name="email"/>')
    print(name_soup.find_all(name="email"))
    print(name_soup.find_all(attrs={"name": "email"}))

def Searching_by_CSS():
    import re
    print(soup.find_all("a", class_="sister"),'\n')
    print(soup.find_all(class_=re.compile("itl")))

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

def css_1():
    css_soup = BeautifulSoup('<p class="body strikeout"></p>')
    print(100*'-', '\n', css_soup.find_all("p", class_="strikeout"))
    print(100*'-', '\n', css_soup.find_all("p", class_="body"))
    print(100*'-', '\n', css_soup.find_all("p", class_="body strikeout"))
    print(100*'-', '\n', css_soup.find_all("p", class_="strikeout body"))
    print(100*'-', '\n', css_soup.select("p.strikeout.body"))
    print(100*'-', '\n', soup.find_all("a", attrs={"class": "sister"}))

def stringargument():
    print(25*'-', 1, 25*'-', '\n', soup.find_all(string="Elsie"))
    print(25*'-', 2, 25*'-', '\n', soup.find_all(string=["Tillie", "Elsie", "Lacie"]))
    import re
    print(25*'-', 3, 25*'-', '\n', soup.find_all(string=re.compile("Dormouse")))
    print(25*'-', 4, 25*'-', '\n', soup.find_all("a", string="Elsie"))
    print(25*'-', 5, 25*'-', '\n', soup.find_all("a", text="Elsie"))

def is_the_only_string_within_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)
def limitargument():
    print(soup.find_all("a", limit=2),'\n')
    for tab in soup.find_all("a", limit=2):
        print(tab)
    
def recursiveargument():
    print(soup.html.find_all("title"))
    print(soup.html.find_all("title", recursive=False))
findall()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-all

#argumento()
#https://beautiful-soup-4.readthedocs.io/en/latest/#the-name-argument

#keywordarg_1()
#keywordarg_2()
#keywordarg_3()
#keywordarg_4()
#Searching_by_CSS()
#print(soup.find_all(class_=has_six_characters))
#css_1()
#https://beautiful-soup-4.readthedocs.io/en/latest/#the-keyword-arguments

#stringargument()
#print(soup.find_all(string=is_the_only_string_within_a_tag))
#https://beautiful-soup-4.readthedocs.io/en/latest/#the-string-argument

#limitargument()
#https://beautiful-soup-4.readthedocs.io/en/latest/#the-limit-argument

recursiveargument()
#https://beautiful-soup-4.readthedocs.io/en/latest/#the-recursive-argument