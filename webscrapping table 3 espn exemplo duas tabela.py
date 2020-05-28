import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
url = 'https://www.espn.com/nba/stats/player/_/season/2017/seasontype/2/table/offensive/sort/avgPoints/dir/desc'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
stat_table = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left') #nome e rank de jogador
stat_table2 = soup.find_all('table', class_ = 'Table Table--align-right') #dados estatisticos

stat_table = stat_table[0]
stat_table2 = stat_table2[0]
rank = []

def pandas1():
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
rank = pandas1()
df = pd.DataFrame(rank[1:], columns=(tuple(rank[0])))
df.to_excel("natalia_linda3.xlsx",index=False)
print('acabou')