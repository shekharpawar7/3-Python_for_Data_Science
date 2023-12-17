import pandas as pd
tech={"coures":["spark","python","spark","hadoop","pandas","python","spark"],
      "fee":[2000,3000,2500,3500,2900,3100,1900],
      "duration":["30days","20days","34days","20days","30days","40days","21days"],
      "discount":[1000,1200,1240,2000,1500,1200,1300]
                  }
df=pd.DataFrame(tech)
df
#groupby single column
df.groupby(["coures"]).mean() #all same coures .mean()
df.groupby(["coures"]).sum()  #all same coures .sum()
 
#groupby multiple columns
df.groupby(["coures","duration"]).sum()


#add index to grouped data

df.groupby(["coures"]).sum().reset_index()   #.reset_index()


