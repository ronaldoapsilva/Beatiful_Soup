import requests
from bs4 import BeautifulSoup

response = requests.get('https://gamefaqs.gamespot.com/', headers = {'User-Agent': 'Mozilla/5.0'})
#print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

a = soup.title
b = soup.get_text(strip=True) #gets rid of new lines
c = soup.find_all(string = 'Vita') #find any string that has the word Vita, vai retorna a lista se tiver mais de uma
d = soup.find_all(string = 'vita') #capitalize muda o resultado

f = type(soup.find_all(string = 'Vita')) 
'''
<class 'bs4.element.ResultSet'> 

ResultSet class is a subclass of a list and not a Tag class which has the find* methods defined. Looping through the results of find_all() is the most common approach: isso precisa, 

AttributeError: 'ResultSet' object has no attribute 'foo' - This usually happens because you expected find_all() to return a single tag or string. But find_all() returns a _list_ of tags and strings–a ResultSet object. You need to iterate over the list and look at the .foo of each one. Or, if you really only want one result, you need to use find() instead of find_all().
'''

g = len(soup.find_all(string = 'Vita')) #usa o len abaixo para saber qual valor atraves do index []
e = soup.find_all(string = 'Vita')[0].find_parents()
h = len(e) #resultado é 10
i = soup.find_all('p', string = 'Vita') # tag p paragraf, = []
j = soup.find_all('a', string = 'Vita') # tag a Defines a hyperlink, = [<a href="/vita">Vita</a>, <a class="notab" href="/vita">Vita</a>, <a href="/vita">Vita</a>]
k = soup.find_all('a', string = 'Vita')[0].get('href') # = /vita





string2 = 'Popular Questions'
l = soup.find_all(string=string2)
m = soup.find_all(string=string2)[0].find_parents() #or l[0].find_parents
n = len(m)
o = m[2] #=index [0]hold the title \ index [1]hold titles \ index [2]hold much more information and you can see the questions
popular_questions = soup.find_all(string=string2)[0].find_parents()[2]
p1 = type(popular_questions) # essa a resposta que precisa ser <class 'bs4.element.Tag'> para fazer o loop abaixo, sem segundo index acima a resposta seria <class 'bs4.element.ResultSet'>
#depois que a popular_questions é a element.tag vc pode usar as tag ol (ordem lista) li (lista), para pegar os resultados
p2 = popular_questions
q = []
#o resulta nao fica clear
for i in popular_questions.find('ol').find_all('li'): 
    q.append(i.get_text())
r = []
#o resulta nao fica clear...mas para entender, achar dentor popular_questions, get_text da tag a( ex abaixo: nao tem resultdo pois a tag 'a' nao tem texto), que esta dentro de 'li', que esta dentro de 'ol'
for i in popular_questions.find('ol').find_all('li'): 
    r.append(i.find('a').get_text())
s = []
#o resulta nao fica clear...strip para remover espacos
for i in popular_questions.find('ol').find_all('li'): 
    s.append(i.get_text().strip())
t = [] #aqui pega as perguntas dentro da lista, que esta dentro da ordem lista, separa os items
for i in popular_questions.find('ol').find_all('li'): 
    t2 = i.get_text().strip().split()
    t3 = ' '.join(t2)
    v = t3.find('?')
    t4 = t3[0:v+1]
    t.append(t4)
resultado = p2
print(resultado)

'''
#lembrar fatiamento aulas do curso em video
string1 = 'Today\'s Featured Top 10' #\ antes do apostofro para escape
t0 = popular_questions.find('ol').find_all('li')[1].get_text()
t1 = popular_questions.find('ol').find_all('li')[1].get_text().strip()
t2 = popular_questions.find('ol').find_all('li')[1].get_text().strip().split()
t3 = ' '.join(t2)
v = t3.find('?')
t4 = t3[0:v+1]
'''