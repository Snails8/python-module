import pandas as pd
from domain.count_column import main

DOWNLOAD_FOLDER = "../../../../../../Downloads/"
FILE_A =  DOWNLOAD_FOLDER + 'test.csv'
FILE_B = DOWNLOAD_FOLDER + 'test.csv'
OUTPUT_PATH = 'data/result.csv'

# df = pd.read_csv(FILE_A, dtype={'code': str})
# print(df['code'])

def main():
  # encoding = 'cp932'
  # df_a = pd.read_csv(FILE_A)
  # df_b = pd.read_csv(FILE_B) 
  
  df = pd.read_csv("../data/test.csv")
  sorted_df = df.sort_values(by='id')
  sorted_df.to_csv("../data/test.csv", index=False)
  
  
  print('--------------- done ------------------')

main()
