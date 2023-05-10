import pandas as pd

DOWNLOAD_FOLDER = "../../../../Downloads/"
FILE_A =  DOWNLOAD_FOLDER + 'testa.csv'
FILE_B = DOWNLOAD_FOLDER + 'test.csv'

OUTPUT_PATH = 'data/result.csv'

def compare_csv_files(file_a: str, file_b: str):
  """csv ファイルを比較し、AにはなくてBにある行をcsvとして出力する

  Args:
      file_a (str): csv_a (比較元)
      file_b (str): csv_b (比較対象)
  """
  
  df_a = pd.read_csv(file_a)
  df_b = pd.read_csv(file_b)
  
  df_diff = df_b.merge(df_a, how='outer', indicator=True).loc[lambda x: x['_merge'] == 'left_only'].drop(columns=['_merge'])
  
  selected_columns = ['code', 'name']
  df_diff = df_diff[selected_columns]
  
  df_diff.to_csv(OUTPUT_PATH)
  print('------------- compare done -----------------')

compare_csv_files(FILE_A, FILE_B)