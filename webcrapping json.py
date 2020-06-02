import requests
import pandas as pd
json = requests.get('https://sik.search.blue.cdtapps.com/au/en/product-list-page?category=bm003&sort=RELEVANCE&size=220&c=plp&v=20200430'
).json()['productListPage']['productWindow']
df = pd.DataFrame.from_dict(json)
print(df)