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
#merge------------------------------(||)add on side (with same index)
df3=pd.merge(df1,df2) #.merge()
df3
"""   coures   fee duration  discount
0   spark  2000   20days      1000
1  python  3000   23days      1500
"""
#concatenate  datafrem-----------------------(=)add on bellow
data=[df1,df2]
df4=pd.concat(data) #.concat()
df4
""" coures     fee duration  discount
A   spark  2000.0   20days       NaN
B  python  3000.0   23days       NaN
C  hadoop  2000.0   21days       NaN
D  pandas  2500.0   30days       NaN
A   spark     NaN      NaN    1000.0
F    java     NaN      NaN    1900.0
B  python     NaN      NaN    1500.0
M      go     NaN      NaN    1200.0
"""
#concate multiple  datafream
df1=pd.DataFrame({"coures":["sprak","pandas","python","go"],
                  "fee":[2000,2100,3000,2900]},index=["A","B","C","d"])

df2=pd.DataFrame({"coures":["hadoop","java","unix","hyper"],
              "duration":["20days","21days","30days","29days"]})

df3=pd.DataFrame({"dicount":[200,300,100,200]})
              
data=[df1,df2,df3]   #adding all 3 datfream in one by one
df5=pd.concat(data)
df5
"""
   coures     fee duration  dicount
A   sprak  2000.0      NaN      NaN
B  pandas  2100.0      NaN      NaN
C  python  3000.0      NaN      NaN
d      go  2900.0      NaN      NaN
0  hadoop     NaN   20days      NaN
1    java     NaN   21days      NaN
2    unix     NaN   30days      NaN
3   hyper     NaN   29days      NaN
0     NaN     NaN      NaN    200.0
1     NaN     NaN      NaN    300.0
2     NaN     NaN      NaN    100.0
3     NaN     NaN      NaN    200.0
"""