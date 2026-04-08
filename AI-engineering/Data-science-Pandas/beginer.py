import pandas as pd

#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

#df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#Pandas Exploration

#get first and last five rows using the builtin function head()and tail()
# get_rows_head = df.head()
# get_rows_tail = df.tail()
#print("first five rows: \n", get_rows_head)
#print("last five rows: \n", get_rows_tail)

#info about the data set
#print(df.info())
# print(df.describe())


#SELECT COLUMNS
# selected_columns = df[["sepal_length", "sepal_width"]]
#print(selected_columns)

#FILTER DATASET

# filter_data = df[(df["sepal_length"] > 5) & (df["species"]  == "setosa")]
# print(filter_data)

#CLEAN | HANDLING MISSING VALUES | RENAME COLUMNS
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", np.nan],
    "Age": [20, 30, np.nan, 82],
    "score": [34, 45, np.nan, 90]
}


data_trans = pd.DataFrame(data)

print(data_trans)