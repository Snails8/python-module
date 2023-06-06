import pandas as pd
import os

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