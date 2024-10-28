import pandas as pd

def main(df1: pd.DataFrame, df2: pd.DataFrame):
  """
  2つのデータフレームをマージする
  日付の丸め処理を行う
  """
  # 時刻をパースして丸める（秒以下を無視）
  df1['time'] = pd.to_datetime(df1['time']).dt.floor('T')
  df2['time'] = pd.to_datetime(df2['time']).dt.floor('T') 

  # カラム名の統一
  df1.rename(columns={'no': 'id', 'time': 'time'}, inplace=True)  

  # データのマージ
  merged_df = pd.merge(df1, df2, on=['bo', 'time'], how='outer', suffixes=('_df1', '_df2')) 

  # 結果をCSVファイルに保存
  merged_df.to_csv('./result/merged_output.csv', index=False)  
  return merged_df