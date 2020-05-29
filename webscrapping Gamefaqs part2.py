from bs4 import BeautifulSoup

html_doc = "C:\\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\webscrapping Gamefaqs part2.html"
soup = BeautifulSoup(open(html_doc), 'html.parser')

a = soup.find_all('div')
#find parents
b = soup.find('div')
c = soup.find(string = 'New York').find_parent()
d = soup.find(string = 'New York').find_parents()
#find_siblings
e = soup.find(string = 'New York').find_next_siblings()
f = soup.find(string = 'New York').find_previous_siblings()
g = soup.find(string = 'New York').find_parent().find_next_siblings()
h = soup.find(string = 'New York').find_parent().find_previous_siblings()
i = soup.find(string = 'New York').find_parent().find_next_sibling().find_previous_siblings()
#find next and previous
j = soup.find(string = 'New York').find_next()
k = soup.find(string = 'New York').find_next().find_next()
l = soup.find(string = 'New York').find_all_next()
m = soup.find(string = 'London').find_all_next()
n = soup.find(string = 'New York').find_previous()  #same as parent
o = soup.find(string = 'New York').find_all_previous() #same as all parents
print(o)