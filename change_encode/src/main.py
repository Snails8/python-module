import pandas as pd

DOWNLOAD_FOLDER = "../../../../Downloads/"
FILE =  DOWNLOAD_FOLDER + 'testa.csv'

OUTPUT_PATH = 'data/result.csv'

def main():
  df = pd.read_csv(FILE, encoding='utf-8')
  
  df.to_csv(OUTPUT_PATH,  encoding='shift_jis', index=False)
  
  print('------------ finish task -----------')

main()