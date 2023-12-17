import pandas as pd
tech1={"coures":["spark","python","hadoop","pandas"],
      "fee":[2000,3000,2000,2500],
      "duration":["20days","23days","21days","30days"]}
index_lables=["A","B","C","D"]
df1=pd.DataFrame(tech1,index=index_lables)
df1

tech2={"coures":["spark","java","python","go"],
       "discount":[1000,1900,1500,1200]}
index_lables=["A","F","B","M"]
df2=pd.DataFrame(tech2,index=index_lables)
df2


#join----join two datafream

#innner join 
df3=df1.join(df2, lsuffix="_left",rsuffix="_right",how="inner")
df3
"""
 coures_left   fee duration coures_right  discount
A       spark  2000   20days        spark      1000
B      python  3000   23days       python      1500"""

#left_join
#when index is don't match the row can drop from datafream
df3=df1.join(df2,  lsuffix="_left", rsuffix= "_right")
df3

#or

df3=df1.join(df2, lsuffix="_left",rsuffix="_right",how="left")
df3
"""
  coures_left   fee duration coures_right  discount
A       spark  2000   20days        spark    1000.0
B      python  3000   23days       python    1500.0
C      hadoop  2000   21days          NaN       NaN
D      pandas  2500   30days          NaN       NaN
"""

#right join
df3=df1.join(df1, lsuffix="_left", rsuffix="_right",how="right")
df3
"""  coures_left  fee_left duration_left coures_right  fee_right duration_right
A       spark      2000        20days        spark       2000         20days
B      python      3000        23days       python       3000         23days
C      hadoop      2000        21days       hadoop       2000         21days
D      pandas      2500        30days       pandas       2500         30days"""

#using columns--------inner
df4=df1.set_index("coures").join(df2.set_index("coures"),how="inner")
"""

        fee duration  discount
coures                         
spark   2000   20days      1000
python  3000   23days      1500"""

#using columns--------left
df4=df1.set_index("coures").join(df2.set_index("coures"),how="left")  
df4    
"""     
   fee duration  discount
coures                         
spark   2000   20days    1000.0
python  3000   23days    1500.0
hadoop  2000   21days       NaN
pandas  2500   30days       NaN
"""    

#using columns--------right
df4=df1.set_index("coures").join(df2.set_index("coures"),how="right")  
df4    
"""
           fee duration  discount
coures                           
spark   2000.0   20days      1000
java       NaN      NaN      1900
python  3000.0   23days      1500
go         NaN      NaN      1200"""