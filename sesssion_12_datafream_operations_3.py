import pandas as pd
technologies={"coures":["spark","pandas","AI","ML","Datascience","c++","SQL"],
              "fee":[2000,3000,4000,3000,3000,3000,4000],
              "duration":["20days","30days","25days","40days","30days","30days","20days"],
              "discount":[0.3,0.300,0.1000,0.1300,0.1000,0.800,0.1000]}
df=pd.DataFrame(technologies)
df

df2=df.query("coures=='spark'")
df2
#or
df1=df.loc[df.coures=="spark"]
df1

#add new column
df 

tutors=["ram","sham","ganesh","ramesh","shekhar","ghansham","papu"]
df2=df.assign(tp=tutors) #any argument
df2

MNCcompanys=["TCS","info","google","tata","bajaj","mahindra","wipro"]
df2=df.assign(tp=tutors,mnc=MNCcompanys)
df2


#df=df.drop({"tutors"},axis=1)
#df2

#add columns in spcific position
df.insert(0,"tutors",tutors) #both name same
df

df["MNCcompanys"]=MNCcompanys #both are same name 

#drive new columns from exsiting columns
df2=df.assign(discount_per=lambda x: x.fee * x.discount /100)
df2

#find count of row
row_count=len(df.index)  #use index
row_count1=len(df.axes[0])  #use axes
row_count2=df.shape[0]   #use shape opration
row_count  #7
row_count1
row_count2

#find count of columns
col_count=len(df.columns) #use index
col_count1=len(df.axes[1])  #use axes
col_count2=df.shape[1]   #use shape opration
col_count  #6
col_count1
col_count2

df.shape  #7,6





























