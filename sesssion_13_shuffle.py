import pandas as pd
tech={"coures":["spark","python","spark","hadoop","pandas","python","spark"],
      "fee":[2000,3000,2500,3500,2900,3100,1900],
      "duration":["30days","20days","34days","20days","30days","40days","21days"],
      "discount":[1000,1200,1240,2000,1500,1200,1300]
                  }
df=pd.DataFrame(tech)
df

#get list of all the column name (header) 
column_head=list(df.columns)
#['coures', 'fee', 'duration', 'discount']
print("The header of datafream is:",column_head)


#pandas shuffle Datafream
df
df2=df.sample(frac=1)  #.sample(frac=1)-----------100%
df2
df3=df.sample(frac=0.5).reset_index()
df3=df.sample(frac=0.5).reset_index(drop=True) #old index can delete
df3
