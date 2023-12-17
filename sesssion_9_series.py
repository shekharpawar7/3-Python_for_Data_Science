#Series
#Series having index and name
#Series is a pne dimensional data like list

import pandas as pd
song2=pd.Series([2,3,4,5,6],name="counts")
print(song2.index)    #RangeIndex(start=0, stop=5, step=1)

song3=pd.Series([23,55,85,74],name="counts",index=["paul","john","george","ringo"])
song3.index     #Index(['paul', 'john', 'george', 'ringo'], dtype='object')
print(song3)
song3[1]        #55 -accessing series
song3.mean()    #59.25
#NaN value
#ignor in arthamatic operation
import pandas as pd
#csv_file
f1=pd.read_csv("age.csv") #relative path used
f1
#excel_file
f2=pd.read_excel("C:/3-Python_for _Data_Science/Bahaman.xlsx") #absolute path
f2

import numpy as np
numpy_ser=np.array([2,3,4,4,5])
numpy_ser       #array([232,323,324,434,425])

numpy_ser[1]    #3
numpy_ser.mean()   #3.6

#dublicate index id allowed
george=pd.Series([21,31,42,65],name="geor",index=["1920","1929","1970","1970"])
george
george["1970"] 

  

#iterating
for i in george:
    print(i)


#updating
george["1970"]=45

#delating
del george["1970"]
george

#convert type
import pandas as pd
song66=pd.Series([3,None,5,11],name="count",index=["george","ringo","john","paul"])
song66.dtypes   #'float64'
pd.to_numeric(song66.apply(str))  #error
pd.to_numeric(song66.astype(str),errors="coerce")  #excute but datatype not change
song66.dtypes


#will replace them given value
song66.fillna(-1)

#nun value can drop
song66.dropna()   #it remove row 

#append / join
song_69=pd.Series([45,18,65,12,87],name="count1",index=["ram","sp","sham","gita","krishna"])
songs=song66.append(song_69)
songs

#...................................................................................
#plotting serices
import matplotlib.pyplot as plt
fig=plt.figure() #line 
song_69.plot()
song66.plot(color="r")
plt.legend()

import matplotlib.pyplot as plt
fig=plt.figure()
song_69.plot( kind="bar",color="g")  #bar
song66.plot( kind="bar",color="r") #bar with color
plt.legend()

#..................................................................................
#histogram
import numpy as np
data=pd.Series(np.random.randn(500),name="random 500")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
