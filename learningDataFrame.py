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

# data = {'color' : ['blue','green','yellow','red','white'],
#         'object' : ['ball','pen','pencil','paper','mug'],
#         'price' : [1.2,1.0,0.6,0.9,1.7]}

# frame = pd.DataFrame(data)
# print(frame)

# You can make a selection of particular rows in the constructor
# frame2 = pd.DataFrame(data, columns=['object', 'price']) # These columns can be in any order
# print(frame2)

# We can also assign a custom index to the DataFrame wih the index arg
# frame2 = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])
# print(frame2)

# frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                # index=['red','blue','yellow','white'],
                # columns=['ball','pen','pencil','paper'])
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
# nestdict = {'red':{2012: 22, 2013: 33},
        #     'white':{2011: 13, 2012: 22, 2013: 16},
        #     'blue': {2011: 17, 2012: 27, 2013: 18}} 
# frame2 = pd.DataFrame(nestdict, index=['red', 'white', 'blue'])
# print(frame2)

# ---------- Transpose a dataframe --------------
# Transpose switches the axis, guess thats what transpose means...?
# print(frame2.T)

# ---------------- Index Objects ----------------
# Index objects are immutable; once declared they cannot be changed
# ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
# idxmin() and idxmax() return the values with the lowest and highest values, respectively
# print(ser.idxmin())
# print(ser.idxmax())



# What about with duplicates in the index?

# serd = pd.Series(range(6), index=['white','white','blue','green', 'green','yellow']) 
# print(serd['white']) # returns 2 rows with 'white' as the index

# data = {'color' : ['blue','green','yellow','red','white'],
        # 'object' : ['ball','pen','pencil','paper','mug'],
        # 'price' : [1.2,1.0,0.6,0.9,1.7]}

# frame = pd.DataFrame(data)

# print(serd.index.is_unique) # False, 'white' appears twice

# print(frame.index.is_unique) # True, each index is unique

# ----------- Other functionalities on indexes ---------------
# This section analyzes in detail Reindexing, Dropping, and Alignment


# ------- Reindexing ----------
# Indexes are immutable, but by using the reindex() function, we can make changes
# ser = pd.Series([2,5,7,4], index=['one','two','three','four'])
# print(ser)
# reindex() actually creates a new series with the old data but the new labels / indexes

# ser.reindex(['three', 'four', 'five', 'one'])
# print(ser)
# the indexs have been changed, but the values remain in the same order
# This is awkward, and imagine having 1000 indexes, its wouldn't be feasible...

# ser3 = pd.Series([1,5,6,3],index=[0,3,5,6])
# print(ser3)
# ser3 = ser3.reindex(range(6),method='ffill')
# print(ser3)

# print(frame)
# frame.reindex(range(5), method='ffill',columns=['colors','price','new', 'object']) 
# print(frame)

# Reindexing is weird and i don't really get it...

# ------- Dropping rows ------------
# This is something I'll likely use

# Drop from a Series

# ser = pd.Series(np.arange(4.), index=['red','blue','yellow','white']) 
# print(ser)

# serdrop = ser.drop('yellow')
# print(serdrop)

# serdrop = ser.drop(['blue', 'white'])
# print(serdrop)

# ************** Drop rows and/or cols from a DataFrame **************************************
# frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                # index=['red','blue','yellow','white'],
                # columns=['ball','pen','pencil','paper'])
# print(frame)

# To drop rows, just pass the row index, axis is optional
# framedrop = frame.drop(['red', 'white'])
# print(framedrop)

# To drop columns you specify the col index, but also specify the axis
# the axis for Columns is 1
# framedrop = frame.drop(['pen', 'pencil'], axis=1)
# print(framedrop)

# ------------------ Arithmetic and Data Alignment --------------------
# s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
# s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])
# print(s1+s2)
# When the labels are present in both operators, their values will be added, 
# while in the opposite case, they will also be shown in the result (new series), but with the value NaN.

# DataFrames can also be aligned

frame1 = pd.DataFrame(np.arange(24).reshape((6,4)),
                index=['red','blue','yellow','white', 'green', 'purple'],
                columns=['ball','pen','pencil','paper'])

frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                index=['blue','green','white','yellow'],
                columns=['mug','pen','ball'])
# print(frame1)
# print(frame2)
# Frame2 does not have the paper col or blue index while
# Frame1 does not have he greemn index or the Mug col

# print(frame1+frame2) # this will add the cells that have a value in both, and display NaN for those that don't

# ---------------- Applying functions ------------------
# Functions by element
# Here we'll use the built in sqrt func from numpy
# print(np.sqrt(frame1))
# there are other built in functions as well, that apply across all cells.


# We can also create userdefined functions and have Pandas apply them across a row or column
def f(x):
        return x.max() - x.min() 

print(frame1.apply(f)) # This applies f() to every row

print(frame1.apply(f, axis=1)) # This applies f() to every column

# A useful case would be to extend the application to many functions simultaneously. 
# In this case, we will have two or more values for each feature applied. 
# This can be done by defining a function in the following manner:

frame1['ball']['red'] = 22
frame1['pencil']['yellow'] =38

def g(x):
        return pd.Series([x.min(), x.max(), (x.max() -x.min())], index=['min','max', 'dif']) 

# in this case the object returned is a dataframe instead of a series, 
# in which there will be as many rows as the values returned by the function.


print(frame1.apply(g).T)

print(frame1.describe())





