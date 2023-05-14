import os
from src.domain.extract_number import get_file_number

PATH = "../../../../Downloads/2023.3"

def rename_files_in_directory(directory_path: str):
  """directory_path: rootから見た相対パス ex) """
  
  print('-------------- start rename filename -------------')
  filenames = os.listdir(directory_path)
  
  for filename in filenames:
    old_path = os.path.join(directory_path, filename)
    
    new_name = get_file_number(filename)
    
    new_filename = new_name + '.jpg'
    new_path = os.path.join(directory_path, new_filename)
    os.rename(old_path, new_path)
    
  print('-------------- finish rename filename -------------')




rename_files_in_directory(PATH)
