import pandas as pd


def main(df: pd.DataFrame):
  """
  2つのカラムで差分がある場合、対象行だけを抽出する
  """
  check_key1 = "test"
  check_key2 = "TEST"
  
  df_diff = __numeric_diff(df, check_key1, check_key2)
  
  df_diff.to_csv("./result/extract_diff.csv", index=False)
  return df_diff

def __numeric_diff(df: pd.DataFrame, key1: str, key2: str):
  """少数系のカラムの差分を計算する
  """
  df[key1] = pd.to_numeric(df[key1], errors='coerce')
  df[key2] = pd.to_numeric(df[key2], errors='coerce')
  
  df['DIFF'] = df[key1] - df[key2]
  df_diff = df[df['DIFF'] != 0]
  
  return df_diff