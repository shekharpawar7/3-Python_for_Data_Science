import pandas as pd
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
              "duration":["20days","30days","25days","40days","30days","30days","20days"],
              "discount":[20,10,15,13,10,25,10]}
index_name=[11,22,33,44,55,66,77]

df=pd.DataFrame(technologies,index=index_name)

df.to_csv("sample.csv")    #CSV file is created 

df.info
#Datafreams Oprations
df.shape   #(7, 4) (row,col)

df.size  #28  col*row

df.columns  #Index(['coures', 'fee', 'duration', 'discount'], dtype='object')

df.columns.values  #array(['coures', 'fee', 'duration', 'discount'], dtype=object)

df.index  #Index([11, 22, 33, 44, 55, 66, 77], dtype='int64')

df.index.values  #array([11, 22, 33, 44, 55, 66, 77], dtype=int64)

df.dtypes  #check datatypes

#acces one column
df["fee"]

#acces more column
df[["fee","discount","coures"]]

#acces one row and all col
df[6:]

#acess value of cell
df["fee"][33]  #4000

#subtracting value form column
df["fee"]-500

#it show count, meaa, std, min , max  of only of int data
df.describe()

df=pd.DataFrame(technologies,index=index_name)
df

#Renameing the column name
df.columns=["a","b","c","d"] #chaining all column name
df

#rename using rename() function
df.rename({"a":"c1","b":"c2"},axis=1)
df.rename({"a":"c3","b":"c4"},axis="columns")
df.rename(columns={"a":"co","b":"cp"})



















