import pandas as pd
file=pd.read_csv("c:/4-dataSets/Seeds_data.csv")
file
df=pd.DataFrame(file)
df

#datafream Opration
df.shape  #(210, 8)

df.info 

df.index #RangeIndex(start=0, stop=210, step=1)

df.columns #['Area', 'Perimeter ', 'Compactness', 'length', 'Width',
       #'Assymetry_coeff', 'len_ker_grove', 'Type']

df.size  #1680

df.describe()

#access area column
df["Area"]

#acces where type =1
df.loc[df.Type==1] 

#find count of row
row_count=len(df.index)  #use index
row_count  #210


#find count of columns
col_count=len(df.columns) #use index
col_count  #8

#add new col using existing col
df=df.assign(avg = lambda x: x.length * x.Width /2)  #.assign()
df["avg"]

#sum of 'length' column
df2=df["length"].sum()     #.sum()
df2   #1181.9920000000002


#mean of 'avg' column
df2=df["avg"].mean()      #.mean()
df2 #9.243447683333333

#find area between 14 to 15
df3=df.loc[df.Area.between(14,15)]
df3

#find Width is more than 4
df4=df.loc[df.Width >4]
df4

#sort 'type' by desending order
df5=df.sort_values(by=["Type"],ascending=[False])  #sort_value
df5

#sort 'Perimeter' by ascending order
df6=df.sort_values(by=["Perimeter"],ascending=[True])  #sort_values
df6

#replace type 1,2,3 as A,B,C
df["Type"]=df["Type"].map({1:"A",2:"B",3:"c"})  #.map()
df

#replace data
df["len_ker_grove"]=df["len_ker_grove"].replace(5,5.232)  #replace()


df[7,"Area"]=15.15


#acces shell data
df[7,"Area"]

#add new row
df.shape #(210, 8)
df.columns
df.loc[211]=[12,14,0.8,5.4,3.7,2.9,5.4,12.1]
df.shape  #(211, 8)

#iterate datafream
for index,row in df.iterrows():   #iterrow()
    print(row["Area"],row["Type"])







