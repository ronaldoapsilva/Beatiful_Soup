import pandas as pd
df = pd.read_json('https://www.theage.com.au/interactive/2020/coronavirus/data-feeder/covid-19-new-cases-json.json?v=3')
print(df)