import os
from domain.extract_number import get_file_number
from domain.rename_increment_number import rename_increment_number
from domain.rename_capture_date import rename_capture_date

DOWNLOAD_PATH = "../../../../Downloads/"
PATH = DOWNLOAD_PATH + "photo/1 test"

def main(directory_path: str):
  """directory_path: rootから見た相対パス ex) """
  
  print('-------------- start rename filename -------------')
  filenames = os.listdir(directory_path)
  
  for i, filename in enumerate(filenames):
    old_path = os.path.join(directory_path, filename)
    
    # new_name = get_file_number(filename)
    new_name = rename_increment_number(filename, i, "20190206") # 数字で連番をつける
    # new_name = rename_capture_date(old_path) # 撮影日からファイル名を生成
    
    new_path = os.path.join(directory_path, new_name)
    os.rename(old_path, new_path)
    
  print('-------------- finish rename filename -------------')




main(PATH)
