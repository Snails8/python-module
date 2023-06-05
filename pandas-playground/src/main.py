import pandas as pd
from domain.count_column import main

DOWNLOAD_FOLDER = "../../../../Downloads/"
FILE_A =  DOWNLOAD_FOLDER + 'test.csv'

# df = pd.read_csv(FILE_A, dtype={'code': str})
# print(df['code'])


main(pd.read_csv(FILE_A))