import re
import os

def rename_increment_number(filename: str, idx: int, yyyymmdd: str | None):
  """
  画像or動画の撮影日からファイル名を生成する
  """
  file_extension = os.path.splitext(filename)[1].lower()

  if file_extension in (".png", ".jpg", ".jpeg"):
      prefix = "IMG_"
      return get_increment_number(filename, idx, yyyymmdd, prefix, file_extension)
      
  elif file_extension in (".mp4", ".mov", ".avi"):
      prefix = "VID_"
      return get_increment_number(filename, idx, yyyymmdd, prefix, file_extension)
  else:
      print(f"{filename} is not a supported media file.")
      return

def get_increment_number(filename: str, idx: int, yyyymmdd: str | None, prefix: str, file_extension: str):
  """ 
  Args:
      filename (str): IMG_20230505_xxxxxx or UNIX 文字列
      idx (int): _description_
  return:
    IMG_20230505_xxxxxx (idx に0追加)
  """
  
  pattern = r'^{re.escape(prefix)}20\d{6}_$'
  match = re.match(pattern, filename)
  
  suffix =  f"{idx:06}"
  if match:
    return match.group() + suffix + file_extension
  else:
    return prefix + yyyymmdd + "_" + suffix + file_extension
  