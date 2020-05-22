#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

html_doc = """<html><head><title>The Dormouse's story</title></head>
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


sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
def example_1():
    print(sibling_soup.prettify())

def next_sibling_and_previous_sibling():
    print(1, '\n', sibling_soup.b.next_sibling)
    print(2, '\n', sibling_soup.c.previous_sibling)

def sibling_2():
    print(sibling_soup.b.string)
    print(sibling_soup.b.string.next_sibling)

def sibling_3():
    link = soup.a
    print(link)
    print(link.next_sibling)
def sibling_4():
    link = soup.a
    print(link.next_sibling.next_sibling)

def sibling_5():
    for sibling in soup.a.next_siblings:
        print(repr(sibling))
def sibling_6():
    for sibling in soup.find(id="link3").previous_siblings:
        print(repr(sibling))
#example_1()
    
'''You can use .next_sibling and .previous_sibling to navigate between page elements that are on the same level of the parse tree:'''
#next_sibling_and_previous_sibling()

'''The strings “text1” and “text2” are not siblings, because they don’t have the same parent:'''
#sibling_2()

'''In real documents, the .next_sibling or .previous_sibling of a tag will usually be a string containing whitespace. Going back to the “three sisters” document:'''
#sibling_3()

'''The second <a> tag is actually the .next_sibling of the comma:'''
#sibling_4()

'''You can iterate over a tag’s siblings with .next_siblings or .previous_siblings:'''
#sibling_5()
sibling_6()