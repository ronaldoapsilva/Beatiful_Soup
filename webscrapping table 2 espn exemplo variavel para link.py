import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
#nao vai funcionar, pois o url nao existe, esse um exemplo onde o final da url muda, quando tem next na pagina para continuar vendo a tabela, o url que funciona somente tem um link showmore
# uma barra invertida siginifca que o codigo continua na proxima linha
num = 1
caminho = Path(r"C:\Users\RONALDOAPARECIDODASI\Documents\MeusProjetos\Treinamento-Python\Beatiful_Soup\basketball_stats table 2 exemplo.txt")
url = 'https://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/count/{}'.format(num)
#headers= {'User-Agent': 'Mozilla/5.0'} 
#headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'} 
#response = requests.get(url, headers = headers)

with open(caminho, 'w') as r:
    r.write('BASKETBALL ASSIST TABLE\n')

while num <272:
    url = 'https://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/count/{}'.format(num)
    time.sleep(1) # para dar tempo de puxa, para caso o servidor esta muito busy
    response = requests.get(url)
    if response.status_code == 200: #200 e codigo para pagina que carrega, outro
        soup = BeautifulSoup(response.content, "html.parser")
        stat_table = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left')
        if len(stat_table) < 2: #para cabo tenha muita tabela na soup do html
            stat_table = stat_table[0]
            with open(caminho, 'a') as r: #a para appending
                for row in stat_table.find_all('tr'):
                    for cell in row.find_all('td'):
                        r.write(cell.text.ljust(22))
                    r.write('\n')
        else:
            print('Too many tables')
    else:
        print('No response')
        print(num)
    #no site de treinamento o site mostra 40 linhas de estatistica por vez
    num += 40