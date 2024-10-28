import pandas as pd

file_a_path = '../data/sample.csv'
file_b_path = '../data/sample2.csv'

common_column = 'common_column'
PR_KEY = 'id'
########################################################
# ２つのcsvを結合し、同じカラム通しの比較を行うscript
# PRキー, common_columnA, common_columnB
########################################################
df_a = pd.read_csv(file_a_path)
df_b = pd.read_csv(file_b_path)

merged_df = pd.merge(df_a[[PR_KEY, common_column]], df_b[[PR_KEY, common_column]], on=PR_KEY, suffixes=('_a', '_b'))
# 結合されたデータフレームの比較や分析をここで行う
# 例: 結合されたデータフレームに何か操作を行う

# 新しいCSVファイルに保存
output_path = '../data/merged.csv'
merged_df.to_csv(output_path, index=False)

print('結合されたデータを保存しました。')
