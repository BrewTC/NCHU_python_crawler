import pandas as pd

df = pd.read_json('123.json')
export_csv = df.to_csv('data.csv', index = None, header = True)