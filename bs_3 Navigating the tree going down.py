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

def Navigating_using_tag_names():
    print(soup.head)
    print(soup.title)
    print(soup.body.b)
    print(soup.a)
    print(soup.find_all('a'))

def contents_children_1():
    head_tag = soup.head
    print(1, "\n", head_tag)
    print(2, "\n", head_tag.contents)
    title_tag = head_tag.contents[0]
    print(3, "\n", title_tag)
    print(4, "\n", title_tag.contents)
    text = title_tag.contents[0]
    #print(text.contents)
    for child in title_tag.children:
        print(5, "\n", child)

def contents_children_2():
    print(len(soup.contents))
    print(soup.contents[0].name)

def descendants_1():
    head_tag = soup.head
    print(head_tag.contents, '\n')
    for child in head_tag.descendants:
        print(child)
    print(len(list(soup.children)))
    print(len(list(soup.descendants)))

def string_1():
    head_tag = soup.head
    title_tag = head_tag.contents[0]
    print(title_tag.string)
    print(head_tag.contents)
    print(head_tag.string)

def strings_and_stripped_strings_1():
    for string in soup.strings:
        print(repr(string))

def strings_and_stripped_strings_2():
    for string in soup.stripped_strings:
        print(repr(string))
#Navigating_using_tag_names()
'''The simplest way to navigate the parse tree is to say the name of the tag you want. If you want the <head> tag, just say soup.head:'''
#contents_children_1()
contents_children_2()
#descendants_1()

#string_1()
'''
If a tag has only one child, and that child is a NavigableString, the child is made available as .string:
If a tag’s only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child:
'''

#print(soup.html.string)
'''If a tag contains more than one thing, then it’s not clear what .string should refer to, so .string is defined to be None:'''

#strings_and_stripped_strings_1()
'''If there’s more than one thing inside a tag, you can still look at just the strings. Use the .strings generator:'''

#strings_and_stripped_strings_2()
'''These strings tend to have a lot of extra whitespace, which you can remove by using the .stripped_strings generator instead:'''