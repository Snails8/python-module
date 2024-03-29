import pandas as pd
import os

DOWNLOAD_FOLDER = "../../../../Downloads/"
FILE_A =  DOWNLOAD_FOLDER + '202303ver05_fix_merge.xlsx'
FILE_B = DOWNLOAD_FOLDER + 'sample.csv'

OUTPUT_PATH = DOWNLOAD_FOLDER + 'result.csv'
OUTPUT_EXCEL_PATH = DOWNLOAD_FOLDER + 'result.xlsx'

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

# compare_csv_files(FILE_A, FILE_B)


def merge_df_add_columns(file_a: str, file_b: str):
  df_a = pd.read_excel(file_a, sheet_name="追加シート")
  df_b = pd.read_csv(file_b)
  
  merged_df = pd.merge(df_a, df_b[['name', 'code', 'is_red', 'is_green']], on='name', how='left')
  
  merged_df.to_csv(OUTPUT_PATH)
  merged_df.to_excel(OUTPUT_EXCEL_PATH)
  print('------------- merge done -----------------')


merge_df_add_columns(FILE_A, FILE_B)

def get_filenames_in_directory(directory):
    filenames = os.listdir(directory)
    return filenames

def check_codes_in_csv(file_list, csv_file):
    # CSVファイルを読み込む
    df = pd.read_csv(csv_file)

    # ファイル名がcode列に含まれているか確認
    for filename in file_list:
        if filename in df['code'].values:
            print(f"{filename} is in the CSV file.")
        else:
            print(f"{filename} is NOT in the CSV file.")
            
file_list = get_filenames_in_directory("../../../../Downloads/2023-3")
check_codes_in_csv(file_list, "data/result.csv")