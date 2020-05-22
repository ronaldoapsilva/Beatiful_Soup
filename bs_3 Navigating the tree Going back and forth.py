#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
;and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

last_a_tag = soup.find("a", id="link3")

def going_back_forth_1():
    print('\n', 1, last_a_tag)
    print('\n', 2, last_a_tag.next_sibling)

    '''But the .next_element of that <a> tag, the thing that was parsed immediately after the <a> tag, is not the rest of that sentence: it’s the word “Tillie”:'''
    print('\n', 3, last_a_tag.next_element)


    print('\n', 4, last_a_tag.previous_element)
    print('\n', 5, last_a_tag.previous_element.next_element)

def going_back_forth_2():
    for element in last_a_tag.next_elements:
        print(repr(element))
#going_back_forth_1()
going_back_forth_2()