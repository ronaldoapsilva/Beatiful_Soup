from bs4 import BeautifulSoup

html_doc = "C:\\Users\RONALDOAPARECIDODASI\Desktop\Standard report.html"
soup = BeautifulSoup(open(html_doc), 'html.parser')

#print(soup.get_text(strip=True))

#config_table = soup.find_all('table', id = "componentDetailsTable")[3].find_all('table')[0].find_all('tr')
config_table = soup.find_all('table', id = "componentDetailsTable")[3].find_all('table')[0]
b = type(config_table)
c = len(config_table)
totrow = len(config_table.find_all('tr'))
print(b, c, totrow)
#print(config_table)
count = 0
Product = 0 
for row in config_table.find_all('tr'):
    if count not in (0, 1, totrow - 1):
        for header in row.find_all('th'):
            print(header.text.strip()[:15].ljust(16), end = '')
            if header.text.strip() == 'Product': Product += 1
            for cell in row.find_all('td'):
                print(cell.text.strip()[:15].ljust(16), end = '')
        count += 1
        print('\n')
    else:
        count += 1
print(Product)        