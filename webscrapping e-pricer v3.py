from bs4 import BeautifulSoup
import pandas as pd
import re
html_doc = "C:\\Users\RONALDOAPARECIDODASI\Desktop\Standard report.html"
soup = BeautifulSoup(open(html_doc), 'html.parser')

#print(soup.get_text(strip=True))

config_table = soup.find_all('table', id = "componentDetailsTable")[3].find_all('table')[0]
#b = type(config_table) <class 'bs4.element.Tag'> c = len(config_table)
totrow = len(config_table.find_all('tr'))
print(totrow)
count = 0
count1 = 0
Product = 0
tabela = []
row_index = 0
app_colum = 0
for row in config_table.find_all('tr'):
    if count not in (0, 1, 2, totrow - 1):
        tag = config_table.find_all('tr')[count]
        if tag.get_attribute_list('bgcolor')[0] == '#CCCCCC': count1 += 1
        #print(count1)
        tabela.append([])
        for header in row.find_all('th'):
            if header.text.strip() == 'Product': Product += 1
            tabela[row_index].append(header.text.strip())
            for cell in row.find_all('td'):
                tabela[row_index].append(cell.text.strip())
        print(len(tabela))
        row_index += 1    
        count += 1
    else:
        count += 1
print(Product)        
print(tabela)
#print(len(tabela))
#df = pd.DataFrame(data=tabela[1:] ,columns=(tuple(tabela[0])))
#df['Quantity'] = df['Quantity'].str.replace(',','.',regex=True) #replace commad by dot
#print(df)
#df.to_excel("testv2.xlsx",index=False)
#df1 = df
#print(df1)

