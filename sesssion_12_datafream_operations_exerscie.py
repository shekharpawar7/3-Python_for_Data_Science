#write pnadas program to create datafream
import pandas as pd
d={"X":[1,2,3,4,5,6,7],
   "Y":[11,22,33,44,55,66,77],
   "Z":[111,222,333,444,555,666,777]}

df=pd.DataFrame(d)  #logic
df

#create datafream and add lables
import pandas as pd
import numpy as np
exam={"name":["sham","ram","gita","papu","ganesh","shiv","sita"],
      "score":[12,23,32,np.nan,21,20,np.nan],
      "attempts":[1,4,2,4,2,1,1],
      "qualify":["yes","no","yes","yes","no","yes","no"]}
lables=["A","B","C","D","E","F","G"]
df=pd.DataFrame(exam,index=lables)
df

#display summay of datafream
import pandas as pd
import numpy as np
exam={"name":["sham","ram","gita","papu","ganesh","shiv","sita"],
      "score":[12,23,32,np.nan,21,20,np.nan],
      "attempts":[1,4,2,4,2,1,1],
      "qualify":["yes","no","yes","yes","no","yes","no"]}
lables=["A","B","C","D","E","F","G"]
df=pd.DataFrame(exam,index=lables)
df

df.describe()  #logic
'''
           score  attempts
count   5.000000  7.000000
mean   21.600000  2.142857
std     7.162402  1.345185
min    12.000000  1.000000
25%    20.000000  1.000000
50%    21.000000  2.000000
75%    23.000000  3.000000
max    32.000000  4.000000
'''

df.info()  #answer
'''
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   name      7 non-null      object 
 1   score     5 non-null      float64
 2   attempts  7 non-null      int64  
 3   qualify   7 non-null      object 
 '''
 
#gate first 3 row
import pandas as pd
import numpy as np
exam={"name":["sham","ram","gita","papu","ganesh","shiv","sita"],
      "score":[12,23,32,np.nan,21,20,np.nan],
      "attempts":[1,4,2,4,2,1,1],
      "qualify":["yes","no","yes","yes","no","yes","no"]}
lables=["A","B","C","D","E","F","G"]
df=pd.DataFrame(exam,index=lables)
df

df.iloc[:3]  #logic
'''
   name  score  attempts qualify
A  sham   12.0         1     yes
B   ram   23.0         4      no
C  gita   32.0         2     yes
''' 

#select name & score from datafream
import pandas as pd
import numpy as np
exam={"name":["sham","ram","gita","papu","ganesh","shiv","sita"],
      "score":[12,23,32,np.nan,21,20,np.nan],
      "attempts":[1,4,2,4,2,1,1],
      "qualify":["yes","no","yes","yes","no","yes","no"]}
lables=["A","B","C","D","E","F","G"]
df=pd.DataFrame(exam,index=lables)
df
df[["name","score"]]  #logic

'''
     name  score
A    sham   12.0
B     ram   23.0
C    gita   32.0
D    papu    NaN
E  ganesh   21.0
F    shiv   20.0
G    sita    NaN
'''
#display spcific part of datafream
import pandas as pd
import numpy as np
exam={"name":["sham","ram","shiv","gita","sita"],
      "score":[23,21,np.nan,19,np.nan],
      "attempts":[2,3,4,1,1],
      "qualify":["yes","no","no","yes","yes"]}
lables=["A","B","C","D","E"]
df=pd.DataFrame(exam,index=lables)
df
df.loc["B":"D","score":"qualify"]  #logic
'''
   score  attempts qualify
B   21.0         3      no
C    NaN         4      no
D   19.0         1     yes
'''

#write a python program to attempt is grether than 2
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[22,32,24,28,19,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
print("following student having a grther than 2 attempt:")
df1=df.loc[df.attempt>2]  #logic
df1
#or
df2=df[df["attempt"]>2]
df2
'''
   name  score  attempt qualify
B   ram     32        3      no
C  sita     24        4      no
'''
#write pandas program to count the number of row and column
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[22,32,24,28,19,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
print(df)
print("number of row in Datafream is",len(df.index)) #logic for row

print("number of columns in Datafream is",len(df.columns)) #logic for col


#pandas program select the row where is missing-NUN
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[22,32,np.nan,28,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
df2=df.loc[df.score.isnull()] #logic-isnull() use to find null value
df2
'''
     name  score  attempt qualify
C    sita    NaN        4      no
E  ganesh    NaN        1     yes
'''
#the row the score is between 15 and 20
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
df.loc[df.score.between(15,20)]  #use between(start,end)


'''
   name  score  attempt qualify
A  sham   19.0        2     yes
B   ram   16.0        3      no'''

#write pandas to selct row where attempt is less than 2
#and score is grather than 15
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df
df2=df[  (df["attempt"]<2) & (df["score"]>15)  ]
df2

#write a change the score in row "d" to 11.5
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df  
df.loc["B","score"]=11.5 #logic
df

#write pandas program to summ of attempt by student
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df  
print(  "total attempt by student:",  df["score"].sum()   ) #.sum()


#write calcate the mean of score
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df  
print(  "total attempt by student:",  df["score"].mean()  ) #.mean()


#add new row 'G'
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df  
df.loc["G"]=["ghansham",28,3,"no"] #add data
df

#write a pandas program to short 
#name in accending order 
#score in descending order
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
df=df.sort_values(by=["name"] ,ascending=[False])#sort_value(by=[] , ascending=[])
df=df.sort_values(by=["score"] ,ascending=[True])#logic
df

#replace qulify column yes and no inpalce True or False
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
df["qualify"] =  df["qualify"].map({"yes":True,"no":False}) #map({})
df

'''
     name  score  attempt  qualify
A    sham   19.0        2     True
B     ram   16.0        3    False
C    sita    NaN        4    False
D    gita   21.0        1     True
E  ganesh    NaN        1     True
F    papu   21.0        2     True
'''

#write program to change the "ganesh" to "rohit" in column
import pandas as pd
import numpy as np
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
df["qualify"] =  df["qualify"].map({"yes":True,"no":False}) #logic
df["name"].replace("ganesh","rohit") #replace(old,new)

#add new column in datafream
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df
AIRrank=[1332,4224,5113,4223,4233,2334]
df.assign(rank=AIRrank)  #.assign(column_name,col_data)
#or
df["rank"]= AIRrank       #df["col_name"] =  col_data
df

#df.drop(["rank","rankd"],axis=1)
df

#iterate the row
exam={"name":["sham","ram","sita","gita","ganesh","papu"],
      "score":[19,16,np.nan,21,np.nan,21],
      "attempt":[2,3,4,1,1,2],
      "qualify":["yes","no","no","yes","yes","yes"]}
labale=["A","B","C","D","E","F"]
df=pd.DataFrame(exam,index=labale)
df


for index,row in df.iterrows():  #.iterrows()
    print(row["name"],row["score"])
    #index-acces the value of index
    #row-acces the value of all row
