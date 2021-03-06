def titulo(msg):
    cores = {'verde':'\033[32m',
            'amarelo':'\033[33m',
            'vermelho':'\033[31m',
            'limpa':'\033[m'}
    print(f'{cores["vermelho"]}{msg}{cores["limpa"]}')
def exemplo(msg2):
    print('{:=^50}'.format(msg2))            

from bs4 import BeautifulSoup
soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', 'html.parser')

def kinds_of_objects():
    titulo("Kinds of objects")
    '''Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. 
    But you’ll only ever have to deal with about four kinds of objects: Tag, NavigableString, BeautifulSoup, and Comment.

    TAG
    A Tag object corresponds to an XML or HTML tag in the original document:'''

    tag = soup.b
    print(type(tag))
    print(tag.name)
    tag.name = "blockquote"
    print(tag)
def atributos():
    exemplo("Attributes")
    '''A tag may have any number of attributes. The tag <b id="boldest"> has an attribute “id” whose value is “boldest”. 
    You can access a tag’s attributes by treating the tag like a dictionary:'''
    tag = soup.b
    print(tag['id'])
    '''You can access that dictionary directly as .attrs:'''
    print(tag.attrs)
    '''You can add, remove, and modify a tag’s attributes. 
    Again, this is done by treating the tag as a dictionary:'''
    tag['id'] = 'verybold'
    tag['another-attribute'] = 1
    print(tag)
def Multi_valued1():
    titulo("Multi-valued attributes")
    '''HTML 4 defines a few attributes that can have multiple values. 
    HTML 5 removes a couple of them, but defines a few more. 
    The most common multi-valued attribute is class (that is, a tag can have more than one CSS class). 
    Others include rel, rev, accept-charset, headers, and accesskey. 
    Beautiful Soup presents the value(s) of a multi-valued attribute as a list:'''
    css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
    print(css_soup.p['class'])
    css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
    print(css_soup.p['class'])
def Multi_valued2():
    '''If an attribute looks like it has more than one value, 
    but it’s not a multi-valued attribute as defined by any version of the HTML standard, 
    Beautiful Soup will leave the attribute alone:'''
    id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
    print(id_soup.p['id'])
def Multi_valued3():
    '''When you turn a tag back into a string, multiple attribute values are consolidated:'''
    rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
    print(rel_soup.a['rel'])
    rel_soup.a['rel'] = ['index', 'contents']
    print(rel_soup.p)
def Multi_valued4():
    '''You can disable this by passing multi_valued_attributes=None as a keyword argument into the BeautifulSoup constructor:'''
    no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
    print(no_list_soup.p['class'])
def Multi_valued5():
    '''You can use `get_attribute_list to get a value that’s always a list, whether or not it’s a multi-valued atribute:'''
    print(id_soup.p.get_attribute_list('id'))
def Multi_valued6():
    '''If you parse a document as XML, there are no multi-valued attributes:'''

    xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml-xml')
    xml_soup.p['class']

def Multi_valued7():
    '''Again, you can configure this using the multi_valued_attributes argument:'''
    class_is_multi= { '*' : 'class'}
    xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
    xml_soup.p['class']

exemplo("NavigableString")
def navigate_1():
    '''A string corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to contain these bits of text:'''
    soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', 'html.parser')
    tag = soup.b
    print(tag.string)
    print(type(tag.string))

def navigate_2():
    '''A NavigableString is just like a Python Unicode string, except that it also supports some of the features described in Navigating the tree and Searching the tree. You can convert a NavigableString to a Unicode string with unicode():'''
    soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', 'html.parser')
    tag = soup.b
    unicode_string = unicode(tag.string)
    print(unicode_string)
    print(type(unicode_string))
def navigate_3():
    soup = BeautifulSoup('<b id="boldest">Extremely bold</b>', 'html.parser')
    tag = soup.b
    tag.string.replace_with("No longer bold")
    print(tag)

#kinds_of_objects()
#atributos()
#Multi_valued1()
#Multi_valued2()
#Multi_valued3()
Multi_valued4()
#Multi_valued5()
#Multi_valued6() #deu erro
#Multi_valued7() deu erro    
#navigate_1()
#navigate_2() deu erro
'''You can’t edit a string in place, but you can replace one string with another, using replace_with():'''
#navigate_3()  

