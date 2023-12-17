#drop row
import pandas as pd
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
                "duration":["20days","30days","25days","40days","30days","30days","20days"],
                "discount":["20%","10%","15%","13%","10%","25%","10%"]}
df=pd.DataFrame(technologies)

#to drop  a row 
df2=df.drop([1,2])  #by name []
df1=df.drop(df.index[[3,4]])  #by index [[]]
df3=df.drop(df.index[2:])  #by  index range 

#if defult indexing use dirct drop()
df1=df.drop(0)  #drop 0 index
df2=df.drop([2,3])  #drop 2,3 index
df3=df.drop(range(2,4))  #drop in range

df4=df.drop(["r1"],axis=0)  #using axis
#.............................................................
#drop columns
import pandas as pd
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
                "duration":["20days","30days","25days","40days","30days","30days","20days"],
                "discount":["20%","10%","15%","13%","10%","25%","10%"]}
df=pd.DataFrame(technologies)

df.drop(["fee"],axis=1) #drop by name
#df.drop(labels=["fee"],axis=1)
#df.drop(columns=["fee"],axis=1)

#if defult index to col
df.drop(df.columns[1],axis=1)   

#inplace=True - it change in original datafream
df.drop(df.columns[1],axis=1,inplace=True)
df

#drop one or more columns by name
df.drop(["fee","coures"],axis=1)
df.drop(columns=["fee","coures"],axis=1)

#drop one or more columns by index
df.drop(df.columns[[1,2]],axis=1)

#drop by list
list_col=["fee","coures"]
df.drop(list_col,axis=1)

