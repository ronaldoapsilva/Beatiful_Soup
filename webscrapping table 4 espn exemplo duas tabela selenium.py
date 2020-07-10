import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
url = 'https://www.espn.com/nba/stats/player/_/season/2017/seasontype/2/table/offensive/sort/avgPoints/dir/desc'

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get(url)

#not required because of silenium 
#response = requests.get(url)

last = None
while not last:
    try:
        last = driver.find_element_by_xpath(
            "//table[@class='Table Table--align-right Table--fixed Table--fixed-left']/tbody/tr[271]/td").text
        # print(last)
    except NoSuchElementException: #precisa importar este erro
        time.sleep(2)
        continue_link = driver.find_element_by_link_text(
            'Show More')  # print(continue_link.text)
        continue_link.click()

soup = BeautifulSoup(driver.page_source, "html.parser")
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
df.to_excel("natalia_linda4.xlsx",index=False)
print('acabou')

driver.close()
