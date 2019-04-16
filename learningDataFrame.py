import numpy as np
import pandas as pd

# The dataframe is a tabular data structure like a spreadsheet. 
# This data structure extends the series structure to multiple dimensions. 
# The dataframe consists of an ordered collection of columns, 
# each of which can contain a value of a different type (numeric, string, Boolean, etc.).

# The DataFrame has two index arrays. 
# The first is the row index, associated with all the values in a row.
# The second is the column label, and is associated will all the values in a column

# A DataFrame is basically a dict of series objects.

data = {'color' : ['blue','green','yellow','red','white'],
        'object' : ['ball','pen','pencil','paper','mug'],
        'price' : [1.2,1.0,0.6,0.9,1.7]}

frame = pd.DataFrame(data)
# print(frame)

# You can make a selection of particular rows in the constructor
frame2 = pd.DataFrame(data, columns=['object', 'price']) # These columns can be in any order
# print(frame2)

# We can also assign a custom index to the DataFrame wih the index arg
frame2 = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])
# print(frame2)

frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                index=['red','blue','yellow','white'],
                columns=['ball','pen','pencil','paper'])
# print(frame3)

# print(frame.index)
# print(frame.columns)

# ---------------- Selecting Columns --------------------
# To display a column by name
# filter by the column name
# print(frame['price'])
# OR use the column name as an attribute of the DataFrame
# print(frame.price)

# ----------------- Selecting Rows ------------------
# print(frame.loc[2]) # Selects row index 2
# # To select multiple rows
# print(frame.loc[[1,3]])
# print(frame[0:2])
# # You can select a specific element like this
# print(frame['object'][3]) # This selects the value at index 3 from object

# ------------- Setting Values --------------------
# frame.index.name = 'id'
# frame.columns.name = 'item'
# print(frame)
# Lets add a new column
# frame['new'] = 12 # creates a new column with value=12 in all rows
# print(frame)
# frame['new'] = [1.9, 3.2, 3.6, 8, 5]
# print(frame)
# frame['new'][1] = 3.3
# print(frame)

# print(frame[frame.isin([1.0, 'pen'])])

# -------------- Deleteing a column ------------

# del frame ['new']
# print(frame)

# -------------- DataFrame from Nested Dict
#This data structure, when it is passed directly as an argument to the DataFrame() constructor, 
# will be interpreted by pandas to treat external keys as column names and internal keys as labels for the indexes. 
# Any fields without a match (red 2011) will be assigned NaN in the df
nestdict = {'red':{2012: 22, 2013: 33},
            'white':{2011: 13, 2012: 22, 2013: 16},
            'blue': {2011: 17, 2012: 27, 2013: 18}} 
frame2 = pd.DataFrame(nestdict, index=['red', 'white', 'blue'])
# print(frame2)

# ---------- Transpose a dataframe --------------
# Transpose switches the axis, guess thats what transpose means...?
# print(frame2.T)

# ---------------- Index Objects ----------------
# Index objects are immutable; once declared they cannot be changed
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
# idxmin() and idxmax() return the values with the lowest and highest values, respectively
print(ser.idxmin())
print(ser.idxmax())



