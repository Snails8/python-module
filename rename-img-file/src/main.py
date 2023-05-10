import os
import re

PATH = "../../../../Downloads/2023.3"

def rename_files_in_directory(directory_path: str):
  """directory_path: rootから見た相対パス ex) """
  
  print('-------------- start rename filename -------------')
  filenames = os.listdir(directory_path)
  
  for filename in filenames:
    old_path = os.path.join(directory_path, filename)
    
    number = extract_number(filename)
    
    if number:
      new_filename = number + '.jpg'
      new_path = os.path.join(directory_path, new_filename)
      os.rename(old_path, new_path)
    else:
      print('error: invalid filename')
      raise
    
  print('-------------- finish rename filename -------------')


def extract_number(filename: str):
  """_summary_
  Args:
      filename (str): ex)1111111_テスト.jpg
  """
  
  pattern = r'\d{8}'
  match = re.search(pattern, filename)
  
  if match:
    return match.group()
  else:
    return None

rename_files_in_directory(PATH)
