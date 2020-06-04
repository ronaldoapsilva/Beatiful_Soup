from bs4 import BeautifulSoup
import pandas as pd
import re
html_doc = "C:\\Users\RONALDOAPARECIDODASI\Desktop\Standard report.html"
soup = BeautifulSoup(open(html_doc), 'html.parser')

#print(soup.get_text(strip=True))

config_table = soup.find_all('table', id = "componentDetailsTable")[3].find_all('table')[0]
#b = type(config_table) <class 'bs4.element.Tag'> c = len(config_table)
totrow = len(config_table.find_all('tr'))
count = 0
tabela = []
row_index = 0
for row in config_table.find_all('tr'):
    if count not in (0, 1, 2, totrow - 1):
        tabela.append([])
        for header in row.find_all('th'):
            tabela[row_index].append(header.text.strip())
            for cell in row.find_all('td'):
                tabela[row_index].append(cell.text.strip())
        row_index += 1    
        count += 1
    else:
        count += 1
df = pd.DataFrame(data=tabela[1:] ,columns=(tuple(tabela[0])))
df['Quantity'] = df['Quantity'].str.replace(',','.',regex=True) #replace commad by dot
print(df)

'''
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("testv4.xlsx")
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='pricer',index=False)
# Get the xlsxwriter workbook and worksheet objects.
Workbook  = writer.book
worksheet = writer.sheets['pricer']
# Add some cell formats.
format1 = Workbook.add_format({'num_format': '0.0'})
format2 = Workbook.add_format({'num_format': '0'})


# Set the column width and format.
worksheet.set_column('E:E', 18, format2)

# Set the format but not the column width.
worksheet.set_column('C:C', None)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
'''

