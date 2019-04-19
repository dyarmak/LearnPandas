import numpy as np
import pandas as pd

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                index=['red','blue','yellow','white'],
                columns=['ball','pen','pencil','paper'])

frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                index=['red', 'blue','yellow', 'white'],
                columns=['ball','pen', 'pencil'])

print(frame2)
frame2['paper'] = np.nan
print(frame2)

colNames = ['pen', 'pencil', 'paper', 'ball', 'mug']

frame2 = frame2.reindex(columns = colNames)
print(frame2)

def paperVal(x):
    if(frame1['pen'] >=5):
        frame1['paper'][x] = 5
    else: 
        frame1['paper'][x] = 0

# df.apply(paperVal)

# df.loc['pen']


# appended = frame1.append(frame2)
# print("Appended Dataframe:")
# print(appended)
