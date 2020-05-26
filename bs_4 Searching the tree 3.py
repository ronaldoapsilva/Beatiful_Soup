from bs4 import BeautifulSoup
html_doc = "C:\\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\html_doc.html"
soup = BeautifulSoup(open(html_doc), 'html.parser')

def find_1():
    print(soup.find_all('title', limit=1))
    print(soup.find('title'))
    print(soup.find("nosuchtag"))
    print(soup.head.title)
    print(soup.find("head").find("title"))

def find_parents_and_parent_1():
    a_string = soup.find(string="Lacie")
    print(a_string)
    print(a_string.find_parents("a"))
    print(a_string.find_parent("p"))
    print(a_string.find_parents("p", class_="title"))

def find_next_siblings_sibling():
    first_link = soup.a
    print(60*'-','\n',first_link)
    print(60*'-','\n',first_link.find_next_siblings("a"))

def find_next_siblings_sibling_2():
    first_story_paragraph = soup.find("p", "story")
    print(first_story_paragraph.find_next_sibling("p"))

def find_previous_siblings_sibling_1():
    last_link = soup.find("a", id="link3")
    print(last_link)
    print(60*'-','\n',60*'-','\n',last_link.find_previous_siblings("a"))

def find_previous_siblings_sibling_2():
    first_story_paragraph = soup.find("p", "story")
    print(first_story_paragraph.find_previous_sibling("p"))

def find_all_next_and_next():
    first_link = soup.a
    print(60*'-','\n',first_link)
    print(60*'-','\n',first_link.find_all_next(string=True))
    print(60*'-','\n',first_link.find_next("p"))

def find_all_previous_and_previous_1():
    first_link = soup.a
    print(60*'-','\n',first_link)
    print(60*'-','\n',first_link.find_all_previous("p"))
    print(60*'-','\n',first_link.find_previous("title"))
#find_1()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find

#find_parents_and_parent_1()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-parents-and-find-parent

#find_next_siblings_sibling()
#find_next_siblings_sibling_2()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-next-siblings-and-find-next-sibling

#find_previous_siblings_sibling_1()
#find_previous_siblings_sibling_2()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-previous-siblings-and-find-previous-sibling


#find_all_next_and_next()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-all-next-and-find-next

#find_all_previous_and_previous()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-all-previous-and-find-previous

find_all_previous_and_previous_1()
#https://beautiful-soup-4.readthedocs.io/en/latest/#find-all-previous-and-find-previous