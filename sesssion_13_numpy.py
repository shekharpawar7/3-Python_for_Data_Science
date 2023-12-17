import pandas as pd
import numpy as np
file={"A":[1,2,3,4,5],
      "B":[2,4,6,8,10],
      "C":[3,6,9,12,15]
      }
df=pd.DataFrame(file)
df

array=np.array(file)
array


#square of col
df["A"]=df["A"].apply(np.square)

