from PIL import Image
from datetime import datetime
import os

def rename_capture_date(filename):
  """
  画像or動画の撮影日からファイル名を生成する
  """
  file_extension = os.path.splitext(filename)[1].lower()

  if file_extension in (".png", ".jpg", ".jpeg"):
      prefix = "IMG_"
      return extract_capture_date(filename, prefix, file_extension)
      
  elif file_extension in (".mp4", ".mov", ".avi"):
      prefix = "VID_"
      return extract_capture_date(filename, prefix, file_extension)
  else:
      print(f"{filename} is not a supported media file.")
      return


def extract_capture_date(filename: str, prefix: str, file_extension: str):
  """
  写真の撮影日からファイル名を生成する
  """
  image = Image.open(filename)
  exif_data = image.getexif()
  capture_date = exif_data.get(36867)  # Exifタグ36867は撮影日時を表す
  
  if capture_date is not None:
    capture_date = datetime.strptime(capture_date, "%Y:%m:%d %H:%M:%S")
    return prefix + capture_date.strftime("%Y%m%d_%H%M%S") + file_extension
  else:
    print(f"{filename} has no capture date.")
    return prefix + filename

