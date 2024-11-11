import pandas as pd


def main(path: pd.DataFrame):
  print("module Extracting columns...")
  
  df = pd.read_csv(path)
  
  df = df[["key", "time", "value"]]
  df = __calc_diff_val(df)
  df.to_csv("./result/extract_column.csv", index=False)
  
  print("module Extracting columns... Done")
  return df
  
def __calc_diff_val(df: pd.DataFrame):
  df["aaa"] = pd.to_numeric(df["aa"], errors='coerce')
  df['bbb'] = df["bbb"].diff()
  df['ccc'] = df['ccc'].fillna(0)
  
  df.to_csv("./result/extract_column.csv", index=False)
  
  return df