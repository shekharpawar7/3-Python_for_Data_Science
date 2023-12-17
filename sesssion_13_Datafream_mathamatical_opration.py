import pandas as pd
import numpy as np
file={"A":[1,2,3,4,5],
      "B":[2,4,6,8,10],
      "C":[3,6,9,12,15]
      }
df=pd.DataFrame(file)
df
#add 7 in All Datafream
def add_7(x):
    return x+7 
df=df.apply(add_7)  #----------------------->.apply()
df
#or
df2=df+7 

#add in spcific col
df=df.A.apply(add_7)
#or
df["A"].apply(add_7)

#add any number in more col
df[["A","B"]].apply(add_7)   #use a [[]] if more col
        #if we apply change in original use
df[["A","B"]]=df[["A","B"]].apply(add_7)

#use lambda function
df.apply(lambda x:x+7)     

df["A"].apply(lambda x:x+7)   #one col

df[["A","B"]].apply(lambda x:x+7)   #mulitiple col

#use .transform()  - same as .apply()
df.transform(add_7)   #--------------------------->.transform()

#use .map()  - same as .apply() , .transform()
df["A"].map(lambda x:x+45)

#square of col
df["A"]=df["A"].apply(np.square)







