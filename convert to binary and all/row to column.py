import pandas as pd

pd.read_csv('train_test.csv', header=None).T.to_csv('transposed.csv', header=False, index=False)
