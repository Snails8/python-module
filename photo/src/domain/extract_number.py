import re

def get_file_number(filename: str):
  """8桁の数値を抽出して返す
  Args:
      filename (str): ex)1111111_テスト.jpg
  """
  number = __extract_number()
  
  if number is None:
      print('error: invalid filename')
      raise ValueError('Invalid filename')
  return number

def __extract_number(filename: str):
  """8桁の数字を抽出、それ以外はNone
  9桁の場合は、最初の8桁を抽出する
  """
  
  pattern = r'\d{8}'
  match = re.search(pattern, filename)
  
  if match:
    return match.group()
  else:
    return None