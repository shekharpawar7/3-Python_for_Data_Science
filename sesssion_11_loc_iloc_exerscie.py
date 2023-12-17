import pandas as pd
file=pd.read_csv("c:/4-dataSets/crime_data.csv")

file
df=pd.DataFrame(file)

df
df.iloc[1]   #acess one row

df.iloc[:3]  #access first 3 row

df.iloc[[2,3]]  #access two row

df.iloc[-1:]  #access last row

df.iloc[-3:]  #access last 3 row

df.iloc[::2] #access alternate row

df["Assault"]  #acccess one columns

df[["Murder","Assault"]]  #access more than one columns use[[]]

df
#acces by index
df.iloc[:,:]  #access all data

df.iloc[1:7,1:4]

df.iloc[:,1:5]

df.iloc[1:23,:]

#access by name
df.loc[1:23,"Murder":"Rape"]

#.....................................................................
import pandas as pd
file=pd.read_csv("C:/4-DataSets/loan.csv")
df=pd.DataFrame(file)
df

df["id"]  #access column

df[["id","member_id"]]  #access two columns

df.iloc[1]  #access one row

df.iloc[[1,2,5,7]]  #access multiple row

df.iloc[2:8]   #access row in range

df.iloc[-1:] #access last row

df.iloc[-3:] #access last 3 row

df.iloc[::2]  #access alternate row

df.loc[2:22,"id":"term"]  #access spceific part

df.iloc[:,3:9]

df.loc[:,"id":"term"]  #access all row and id to term col

df.loc[:,"id":"term":2] #alternate 2

#...................................................................
import pandas as pd
file=pd.read_csv("C:/4-DataSets/bank_data.csv")
df=pd.DataFrame(file)
df
df["age"]  #access age columns

df[["age","loan"]]  #access loan and age col

df.iloc[7]  #access 7 row 

df.iloc[3:7] #acces multiple row

df.iloc[:,1:8]  #access all row and some columns

df.iloc[1:5,:]   #access all columns and some row

df.loc[:,"age":"pdays"]  #access all row and some column by name

df.loc[1:9,"age":"pdays"]

df.iloc[1:9,1:8]

df.iloc[-1:]  #acces last row

df.iloc[:,:2]  #all row and columns alternate

