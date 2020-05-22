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


'''You can access an element’s parent with the .parent attribute. In the example “three sisters” document, the <head> tag is the parent of the <title> tag:'''
title_tag = soup.title
print(1, title_tag)
print(2, title_tag.parent)

'''The title string itself has a parent: the <title> tag that contains it:'''
print(3, title_tag.string.parent)


'''The parent of a top-level tag like <html> is the BeautifulSoup object itself:'''
html_tag = soup.html
print(4, type(html_tag.parent))

def parents_1():
    link = soup.a
    print(link)
    for parent in link.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)

'''You can iterate over all of an element’s parents with .parents. This example uses .parents to travel from an <a> tag buried deep within the document, to the very top of the document:'''
parents_1()