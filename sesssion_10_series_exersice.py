#write a program for create a series
import pandas as pd
series=pd.Series([2,4,6,8,10])
series


#write a program to series into listimport pandas as pd and its type
series=pd.Series([2,4,6,8,10])
print("pandas series and its type:")
series
series.dtypes

print("convert into list:")
print(type(series.to_list()))  #1 method-list
print(type(list(series)))     #2method-list

#...................................................................................
#write a pandas program to add , subtract ,  muliple and  divde
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([4,8,12,16,18])

ds=ds1 + ds2
print("addition:",ds)

ds=ds2-ds1
print("subtraction:",ds)

ds=ds1*ds2
print("multiplication:",ds)

ds=ds1/ds2
print("division:",ds)

#...................................................................................\
#compare element in two series
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2-pd.Series([1,3,5,4,6])
print("series first:")
print(ds1)
print("series second:")
print(ds2)
print("Compare series!!!!!!!!!!")

print("equal are")
print(ds1==ds2)

print("less than:")
print( ds1<ds2)

print("greather than:")
print(ds1 >ds2)

#...................................................................................
#write python program to convert  dictnory to serirs
import pandas as pd
dit={"a":100,"b":200,"c":300,"d":400}
new_series=pd.Series(dit)
print("converted series :") 
new_series

#..................................................................................
#write python program to convert numpy array to series
import pandas as pd
import numpy as np
num=np.array([1,3,4,6,2,9])
new_serire=pd.Series(num)
print("converted series:")
print(new_series)

#...............................................................................
#change a data type of given series/col
import pandas as pd
s1=pd.Series(["a","b","c","d","400"])
s1.dtype

print("Convert into string")
print(s1.convert_dtypes())   #string


print("convert into object")
print(s1.astype("str"))    #object

print("convert into numeric")
print(pd.to_numeric(s1,errors="coerce")) #float

#...............................................................................
#write a python program to convert datafrem to series (print first col)
import pandas as pd
tech={"dept":["computer","mech","civil"],
      "fee":[30000,20000,25000],
      "code":["co20","co24","co31"]
      }
df=pd.DataFrame(tech)
df
s1=df.iloc[:,0]  #acces as a serires
s2=df.iloc[1:2,]  
print(s1)
print(s1.dtype)      #object
series=pd.Series(s1)
print("First col as series:",series)
print(series.dtype)

#..................................................................................

import pandas as pd
s=pd.Series([["red","black","green"],
            ["red","blue","white"],
            ["red","green","yellow"]])
print("orignial series:")
print(s)
s=s.apply(pd.Series)
print(s)
s=s.stack()
print(s)
s=s.reset_index(drop=True)
print("one serirs:")
print(s)
#..................................................................................
#write a program to add DATA int existing series
import pandas as pd
s1=pd.Series(["200","html","python","300.02","300"])
print("original series:")
print(s1)

new=pd.concat([s1, pd.Series([500,"php"])],ignore_index=True)
print(new)

#...............................................................................
#write a pndas program to sort a give serirs
s=pd.Series(["100","500","300","200","python","400","600"])
print("original serire:")
print(s)
#s.sort_values()
new_s=pd.Series(s).sort_values()
print(new_s)



#..................................................................................
#write a pandas program to change the order of index of given series
import pandas as pd
s=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(s)

s=s.reindex(index=["b","a","c","d","e"])
print(s)