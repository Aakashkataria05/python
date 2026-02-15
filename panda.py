import pandas as pd

s1 = pd.Series([32,44,22,33,77])
print(s1)

data = {
    "name" : ["Aakash","kartik","daksh"],
    "age" : [21,22,20],
    "city" : ["delhi","himachal","haryana"]
}
print(pd.DataFrame(data))