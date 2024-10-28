import pandas as pd

def main(df: pd.DataFrame):
  
  # "label"カラムが存在するかどうか確認
  if 'label' in df.columns:
    print("labelカラムが存在します。")
  else:
    return print("labelカラムが存在しません。")
  
  
  # "label"カラムの値の出現回数を集計
  print(df['label'].value_counts())
