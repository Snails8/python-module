import re

def get_increment_number(filename: str, idx: int, yyyymmdd: str | None):
  """ 
  Args:
      filename (str): IMG_20230505_xxxxxx or UNIX 文字列
      idx (int): _description_
  return:
    IMG_20230505_xxxxxx (idx に0追加)
  """
  
  pattern = r'^IMG_20\d{6}_$'
  match = re.match(pattern, filename)
  
  if match:
    return match.group() + f"{idx:06}"
  else:
    return "IMG_" + yyyymmdd + "_" + f"{idx:06}"
  