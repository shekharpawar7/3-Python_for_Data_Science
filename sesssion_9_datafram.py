import pandas as pd
pd.__version__   #check pandas version

import pandas as pd
#create datafream from list
technologies=[["spark",20000,"30days"]  ,  ["pandas",30000,"40days"],["Ai",4000,"50days"]]
df=pd.DataFrame(technologies)
df

#name to row and columns
col_name=["coures","fees","durestion"]
row_name=[1,2,3]
df=pd.DataFrame(technologies,columns=col_name,index=row_name) #name to row and columns
df

#check datatype
df.dtypes


#using dictnoery
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
                "duration":["20days","30days","25days","40days","30days","30days","20days"],
                "discount":["20%","10%","15%","13%","10%","25%","10%"]}
df=pd.DataFrame(technologies)
df.dtypes

#convert all into string
df2=df.convert_dtypes() 
df2.dtypes

#convert all into object
df2=df.astype(str)   
df2.dtypes

#convert spacific col
df2=df.astype({"fee":int,"discount":str})
df2.dtypes        
  
#convert all col in same dataytype      
cols=["fee","duration"] 
df2=df[cols].astype(str)     
df2.dtypes        
        
#ignore error
df2=df.astype({"discount":int},errors="ignore")       
df2.dtypes 

#generate errore
df2=df.astype({"coures":str},errors="raise")      
df2.dtypes 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        