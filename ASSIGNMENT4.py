import pandas as pd
import numpy as np
import seaborn as sbn

#1 How to import pandas and check the version?


print(pd.__version__)

#2 How to create a series from a numpy array?

a=np.array([1,2,3,4,5])
b=pd.Series(a)
print(b)

#3 How to convert the index of a series into a column of a dataframe?
df=pd.DataFrame(a)
df['index']=b.index
print(df)
#4 Write the code to list all the datasets available in seaborn library.

print(sbn.get_dataset_names())
# 4 Write the code to list all the datasets available in seaborn library. Load the 'mpg' dataset

data=sbn.load_dataset('mpg')
print(data)

#5 Which country origin cars are a part of this dataset?
data['origin'].unique()

#6 Extract the part of the dataframe which contains cars belonging to 'usa'

data[data['origin']=='usa']






