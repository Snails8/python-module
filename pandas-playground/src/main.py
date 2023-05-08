import pandas as pd

df = pd.read_csv('data/output.csv', dtype={'code': str})

print(df['code'])