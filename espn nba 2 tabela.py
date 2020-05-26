import requests
from bs4 import BeautifulSoup
from pathlib import Path

url = 'https://www.espn.com/nba/stats/player/_/season/2017/seasontype/2/table/offensive/sort/avgPoints/dir/desc'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
stat_table = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left') #nome e rank de jogador
stat_table2 = soup.find_all('table', class_ = 'Table Table--align-right') #dados estatisticos

stat_table = stat_table[0]
stat_table2 = stat_table2[0]
rank = []
def teste1():
    for i, row in enumerate(stat_table.find_all('tr')): 
        rank.append([])
        if i == 0:
            for header in row.find_all('th'):
                rank[i].append(header.text)
        else:
            for cell in row.find_all('td'):
                rank[i].append(cell.text)         
    for i, row in enumerate(stat_table2.find_all('tr')): 
        if i == 0:
            for header in row.find_all('th'):
                rank[i].append(header.text)
        else:
            for cell in row.find_all('td'):
                rank[i].append(cell.text)   
    return rank    
tabela = teste1()
print(tabela)

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
    caminho = Path(r"C:\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\basketball_stats2.txt")
    with open(caminho, 'w') as r:
        for row in stat_table2.find_all('tr'):
            for cell in row.find_all('td'):
                r.write(cell.text.ljust(5))
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
Each table row is defined with the <tr> tag. A table header is defined with the <th> tag. By default, table headings are bold and centered. A table data/cell is defined with the <td> tag.
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