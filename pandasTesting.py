
import pandas as pd

list_test = []

tuple1 = ("HAYDEN", "ANDY", "BURAK", "ASA")
tuple2 = ("WORCESTER", "BRUM", "INSTANBUL", "MK")

list_test.append(tuple1)
list_test.append(tuple2)

print(tuple1, tuple2, list_test)

df = pd.DataFrame(list_test)

df.columns = ["HMB", "AP", "BD", "AT"]

print(df)
df.to_csv("HMB Test.csv")