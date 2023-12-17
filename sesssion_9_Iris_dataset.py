import pandas as pd

file=pd.read_csv("c:/4-datasets/iris.csv")
df=pd.DataFrame(file)
df
df.shape  #(150, 5)

df.index  #start=0, stop=150, step=1
    
df.dtypes
"""
sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
species          object
"""

#all columns in the float we convert into int 
df=df.astype({"sepal_length":int,"sepal_width":int,"petal_length":int,"petal_width":int})
df.dtypes
"""
sepal_length     int32
sepal_width      int32
petal_length     int32
petal_width      int32
species         object
dtype: object
"""


df.columns  #['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']
#...............................................................................

#add 7 in datafream using-----.apply()
def add_7(x):
    return x+7
df["sepal_length"]
df["sepal_length"]=df["sepal_length"].apply(add_7) #.apply()
df["sepal_length"]

#subtract 4 in datafream using-----.transform()
df["sepal_length"]
def sub_16(x):
    return x-4
df["sepal_length"].transform(sub_16)#.tranform()
df["sepal_length"]

#multiple with 8 using----------------.map()
df["sepal_length"]
def mul_8(x):
    return x*8
df["sepal_length"].map(mul_8)#.map()
df["sepal_length"]

#add 7 in multiple columns

df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].apply(add_7)

#using lambda function multiple 100
fun=lambda x:x*100
df["sepal_length"].apply(fun)

#multiple with 900
df["sepal_length"]=df["sepal_length"].apply(lambda x:x*900)

#.................................................................................................

#make square of columns
import numpy as np
df["sepal_length"]
df["sepal_length"]=df["sepal_length"].apply(np.square)
df["sepal_length"]

#..................................................................................................
#.gruopby()
df
df.groupby(["sepal_length"]).sum()

df.groupby(["sepal_width"]).mean()

#gruopby with new index
df.groupby(["sepal_length"]).sum().reset_index()

#.............................................................................

#make list of all columns in datafream
col_list=list(df.columns)
print("the columns in list is ",col_list)
     #the columns in list is  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
     
#...............................................................................................
#shuffle
df1=df.sample(frac=1)

#shuffle with new index
df1=df.sample(frac=1).reset_index()
df1

#shuffle with removing old index
df2=df.sample(frac=1).reset_index(drop=True)
df2
