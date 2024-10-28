import pandas as pd
from _module import merge_csv, extract_column, compare_2column

csv1 = "./output.csv"
csv2 = "./all.csv"

extract_csv = "./input/sample.csv"

merge_csv1 = "./result/extract_column.csv"
merge_csv2 = "./input/test.csv"

def main():
  df = extract_column.main(path=extract_csv)
  
  
  # preprocess
  df1 = pd.read_csv(merge_csv1)
  df2 = pd.read_csv(merge_csv2)  
  df1 = df1[["key", "timeA", "value", "value2"]] 
  df2 = df2[["no", "time", "value"]]
  
  df = merge_csv.main(df1, df2)
  
  compare_2column.main(df)

if __name__ == "__main__":
  main()