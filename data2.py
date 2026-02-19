import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/kirenz/datasets/master/data-ex-61.csv")
print(df['Date'])
print(df.loc[1])