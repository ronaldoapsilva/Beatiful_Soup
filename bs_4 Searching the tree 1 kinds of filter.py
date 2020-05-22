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

'''
Kinds of filters

Before talking in detail about find_all() and similar methods, I want to show examples of different filters you can pass into these methods. These filters show up again and again, throughout the search API. You can use them to filter based on a tag’s name, on its attributes, on the text of a string, or on some combination of these.
'''
def string():
    print(soup.find_all('b'))
    '''If you pass in a byte string, Beautiful Soup will assume the string is encoded as UTF-8. You can avoid this by passing in a Unicode string instead.'''

def regular_expression_1():
    import re
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)

def regular_expression_2():
    import re
    for tag in soup.find_all(re.compile("t")):
        print(tag.name)

def lista():
    for tag in (soup.find_all(["a", "b"])):
        print(tag)

def lista_2():
    for tag in soup.find_all(True):
        print(tag.name) #print(tag.string)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def not_lacie(href):
    import re
    return href and not re.compile("lacie").search(href)
    
    

#string()
'''The simplest filter is a string. Pass a string to a search method and Beautiful Soup will perform a match against that exact string. This code finds all the <b> tags in the document:'''

#regular_expression_1()
'''If you pass in a regular expression object, Beautiful Soup will filter against that regular expression using its search() method. This code finds all the tags whose names start with the letter “b”; in this case, the <body> tag and the <b> tag:'''

#regular_expression_2()
'''This code finds all the tags whose names contain the letter ‘t’:'''

#lista()
'''A list
If you pass in a list, Beautiful Soup will allow a string match against any item in that list. This code finds all the <a> tags and all the <b> tags:'''

#lista_2()
'''The value True matches everything it can. This code finds all the tags in the document, but none of the text strings:'''

#print(soup.find_all(has_class_but_no_id))
'''A function
If none of the other matches work for you, define a function that takes an element as its only argument. The function should return True if the argument matches, and False otherwise.
Here’s a function that returns True if a tag defines the “class” attribute but doesn’t define the “id” attribute:'''
'''This function only picks up the <p> tags. It doesn’t pick up the <a> tags, because those tags define both “class” and “id”. It doesn’t pick up tags like <html> and <title>, because those tags don’t define “class”.'''

#print(soup.find_all(href=not_lacie))
'''If you pass in a function to filter on a specific attribute like href, the argument passed into the function will be the attribute value, not the whole tag. Here’s a function that finds all a tags whose href attribute does not match a regular expression:'''


'''
#The function can be as complicated as you need it to be. Here’s a function that returns True if a tag is surrounded by string objects:
from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)
'''