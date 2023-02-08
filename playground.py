import pandas as pd

df = pd.read_csv("data.csv",sep=";")

for index,row in df.iterrows():
    print (row["title"])