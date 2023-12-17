#if we use more than two index use[[]]

#slicing operater------

#loc[] - use when work with lebles   
#iloc[]- use when work with indexs

#[ start_row : end_row  ,  start_col : end_col ]

import pandas as pd
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
              "duration":["20days","30days","25days","40days","30days","30days","20days"],
              "discount":[20,10,15,13,10,25,10]}
index_name=[11,22,33,44,55,66,77]

df=pd.DataFrame(technologies,index=index_name)
df

#access cell
df["fee"][22] #---------->[col][row]




#...................................................................
#select whole rows only by index
df.iloc[3]

#select more index of row
df.iloc[[2,3,4]]            #if we use more than two index use[[]]

#first row
df.iloc[:1]                 #loc[:end_row_index]

#acces in range
df.iloc[2:6]               #loc[start_row_index:end_row_index]

#first 3 row
df.iloc[:3]

#last row
df.iloc[-1:]

#last 3 row
df.iloc[-3:]

#select alternate row
df.iloc[::2]



#..................................................................
#acces whole row by name
df.loc[11]

#acces more row
df.loc[[11,22,44]]

#first row
df.iloc[:11]   ##loc[:end_row_name]

#acces in range 
df.loc[11:44]   #loc[start_row_name:end_row_name]

#alternate
df.loc[11:55:2]


#..................................................................
#select whole columns only by name

#access colums
df["fee"]

#access more than one col
df[["fee","coures"]]


###################################################################
#acces some part by index----------------------------------iloc[:]

df
#access all rows & some cols 
df.iloc[:,1:4]         #[ : , start_col_index:end_col_index ]

#accesss all columns & some rows
df.iloc[2:5,:]         #[ stat_row_index:end_row_index , : ]

#access specific part row&col
df.iloc[1:4,5:7]    

#acces all row & alternate cols
df.iloc[:,1:5:2]     #[:,start_col:end_col:step]

#..................................................................

#acces some part by name------------loc[:]

#access all rows & some cols
df.loc[:,"coures":"duration"] #[ : , start_col_name:end_col_name ]

#accesss all columns & some rows
df.loc[22:55,:]       #[ stat_row_name:end_row_name, : ]

#access specific part row&col
df.loc[11:44,"coures":"duration"]

#acces all row & alternate cols
df.loc[:,"coures":"discount":2]     #[:,start_col:end_col:step]

#...................................................................


