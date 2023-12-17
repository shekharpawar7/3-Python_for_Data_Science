import pandas as pd
file=pd.read_csv("c:/4-datasets/iris.csv")
df=pd.DataFrame(file)
df
#................................................................................
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
#...................................................................................
#slicing opration
df.index

df.columns  #['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species']

df.size #750

df.shape #(150,5)
#.................................................................................
#loc & iloc

#acces one row
df.iloc[7]

#acces first 3 row
df.iloc[:3]

#acces last 3 row
df.iloc[-3:]

#acces all alternet row
df.iloc[::2]

#acces column
df["sepal_length"]

#access cell of datafream
df["sepal_length"][7] #5.0


#sub 5 from columns
df["sepal_length"]-5

#acces columns where sepal_length=5
df.loc[df.sepal_length==5]

#sum of columns
df["sepal_length"].sum() #876.5

#mean of columnd
df["sepal_length"].mean()  # 5.84333333

#add new col using existing columns
df=df.assign(avg_sepal=lambda x : x.sepal_length  * x.sepal_width)
df

#iterrate a row
for i,row in df.iterrows():
    print(row["sepal_length"])

#...............................................................................
#drop one row
df.drop(0)

#drop multi row
df.drop([1,2,3])

#drop row range
df.drop(range(6,10))

#drop one column
df
df.drop(["sepal_length"],axis=1)

#drop multiple column
df.drop(["sepal_length","petal_length"],axis=1)
#.........................................................................

#rename
df
df.rename({"sepal_length":"s_length","petal_length":"p_length"},axis=1)

#...............................................................................

#.apply()
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
