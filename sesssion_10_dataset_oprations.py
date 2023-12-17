#...................................................................
#bank_data 
import pandas as pd
file=pd.read_csv("C:/4-DataSets/bank_data.csv")
df=pd.DataFrame(file)
df

#finding datatype
df.dtypes

#finding shape
df.shape             #(45211, 32)

#finding size
df.size            #1446752

#finding index
df.index  #RangeIndex(start=0, stop=45211, step=1)

#finding column
df.columns  
'''
['age', 'default', 'balance', 'housing', 'loan', 'duration', 'campaign',
'pdays', 'previous', 'poutfailure', 'poutother', 'poutsuccess',
'poutunknown', 'con_cellular', 'con_telephone', 'con_unknown',
'divorced', 'married', 'single', 'joadmin.', 'joblue.collar',
'joentrepreneur', 'johousemaid', 'jomanagement', 'joretired',
'joself.employed', 'joservices', 'jostudent', 'jotechnician',
'jounemployed', 'jounknown', 'y']
'''
#convert into string
file=pd.read_csv("C:/4-DataSets/bank_data.csv")
df=pd.DataFrame(file)
df
df.dtypes
df.convert_dtypes()
df.dtypes

#convert into object
df.astype("str")
df.dtypes

#change name of columns
df.columns
df=df.rename({"age":"persone_age","loan":"loan_amount"},axis=1)
df.columns

#acces only one columns
df.iloc[:,0]

#data type to spacific col
df1=df.astype({"balance":float})
df1.dtypes        #balance        -   float64

#- 500 from loan amount
df["loan_amount"]-500

#acces one col
df["balance"]

#access more than one col
df[["balance","pdays"]]  #acces one more col use[[]]

#acess value of cell
df["balance"][9]  #593

#export to csv
df.to_csv("bank.csv")


#drop row by index
df
df1=df.drop([0])  #drop first row by index
df1

df1=df.drop(df.index[[2,4,3]]) #drop multi row by index
df1


#........................................................................
#loan
import pandas as pd
file=pd.read_csv("C:/4-DataSets/loan.csv")
print(file)
df=pd.DataFrame(file)
print(df)

df.shape   #(39717, 111)

df.size   #4408587

df.index  #RangeIndex(start=0, stop=39717, step=1)
df.index.values  #[    0,     1,     2, ..., 39714, 39715, 39716],

df.columns
'''
['id', 'member_id', 'loan_amnt', 'funded_amnt', 'funded_amnt_inv',
       'term', 'int_rate', 'installment', 'grade', 'sub_grade',
       ...
       'num_tl_90g_dpd_24m', 'num_tl_op_past_12m', 'pct_tl_nvr_dlq',
       'percent_bc_gt_75', 'pub_rec_bankruptcies', 'tax_liens',
       'tot_hi_cred_lim', 'total_bal_ex_mort', 'total_bc_limit',
       'total_il_high_credit_limit']
'''
df.dtypes

df["member_id"]
 
df[["member_id","grade"]]

df.columns
df1=df.rename({"num_tl_90g_dpd_24m":"24m","percent_bc_gt_75":"75m"},axis=1)
df1.columns

df.head(3)
df
#acces cell
df["term"][7]   #[col][row]

#acess part of df
df.loc[0:7,"id":"term"] #[row_start:row_end , col_start:col_end]
df.head(5)
 
df2=df.loc[df.term==" 36 months"]


#...................................................................
#crime_data
import pandas as pd
file=pd.read_csv("c:/4-dataSets/crime_data.csv")
df=pd.DataFrame(file)
df

df.head()
df.shape
df.size
df.index
df.index.values
df.columns.values
df
df[" "]="name"
del df[" "]
df.rename({" ":"name"},axis=1)
df.columns=["name","muder","Assault","urbanPop","Rape"]
df
df.index
df.columns
df.dtypes
df=df.astype({"muder":int})
df1=df.loc[df.muder==12]
