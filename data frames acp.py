import pandas as pd
import numpy as np
exam_data={'names':['boom','koom','zoom','boos','bam'],
           'scores':[2,3,4,5,6],
           'grade':[1,2,3,4,5],
           'subjects':['maths','english','hindi','science','sst']}
labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=labels)
print("summary:")
print(df.info())