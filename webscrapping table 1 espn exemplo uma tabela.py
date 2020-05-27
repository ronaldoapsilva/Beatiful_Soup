import requests
from bs4 import BeautifulSoup
from pathlib import Path
#if the example below try the on below

url = 'https://www.espn.com/nba/stats/player/_/season/2017/seasontype/2/table/offensive/sort/avgPoints/dir/desc'


response = requests.get(url) 
'''
se der erro precisa- usar as opcoes abaixo, vai para final do codigo para mais informacao

option 1 
headers= {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers = headers)

option 2 
headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'} 
response = requests.get(url, headers = headers)

Option 3 
headers= {'User-Agent': 'Chrome 83 on Windows 10'}
response = requests.get(url, headers = headers)
'''

#print(response.status_code)
#print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
stat_table = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left')

stat_table = stat_table[0]



def test1():
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
            print(cell.text)
test1()
#imprimir resultado
def test2():
    caminho = Path(r"C:\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\basketball_stats.txt")
    with open(caminho, 'w') as r:
        for row in stat_table.find_all('tr'):
            for cell in row.find_all('td'):
                r.write(cell.text)
#test2()        
#cria o txt, copia cell.txt para o arquivo
def test3():
    caminho = Path(r"C:\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\basketball_stats.txt")
    with open(caminho, 'w') as r:
        for row in stat_table.find_all('tr'):
            for cell in row.find_all('td'):
                r.write(cell.text)
            r.write('\n')
#test3()        
#cria o txt, copia cell.txt para o arquivo e pula uma linha cada interacao
def test4():
    caminho = Path(r"C:\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\basketball_stats.txt")
    with open(caminho, 'w') as r:
        for row in stat_table.find_all('tr'):
            for cell in row.find_all('td'):
                r.write(cell.text.ljust(22))
            r.write('\n')
#test4()        
#cria o txt, copia cell.txt para o arquivo e pula uma linha cada interacao, e ajusta os dados de td para 22, completando com o espaco
'''
ljust exemploe
str = 'This is what ljust does'
print(str.ljust(100, '#'))
'''
print('acabou')
'''
Each browser has a specif header to communicate with web site, so web site know the your brorser and operation sistem


below how to know your broser user-agent
https://www.whatismybrowser.com/detect/what-is-my-user-agent
Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0

url = 'https://www.espn.com/nba/stats/player/_/season/2017/seasontype/2/table/offensive/sort/avgPoints/dir/desc'
headers= {'User-Agent': 'Mozilla/5.0'} 
response = requests.get(url, headers = headers)

make sure the status code is 200 to pull everything
print(response.status_code)
'''
'''
https://www.w3schools.com/html/html_tables.asp
Defining an HTML Table

An HTML table is defined with the <table> tag.

Each table row is defined with the <tr> tag. A table header is defined with the <th> tag. By default, table headings are bold and centered. A table data/cell is defined with the <td> tag.

"Table"=Starts a table.
"TR" (Table Row) = Starts a row.
"TD" (Table Data) = Starts a  cell to enter a data.
"/TD" = Puts an end to a data entry.
"/TR" = Puts an end to a row.
"/Table" = Ends Table.
'''

'''
o codigo abaixo indica qtas tables tem, no caso uma
print(len(stat_table))
stat_table is not a table, but a resultset per type codigo below
print(type(stat_table))
como temos uma tabela, para extrair ela, precisamos "zero elemento" abaixo (se tiver mais de uma tabela precisa descobrir qual) indica que vamos extrair resultado dessa unica tabela,
stat_table = stat_table[0] 
print(type(stat_table)) a resposta abaixo tag
#<class 'bs4.element.Tag'>
'''